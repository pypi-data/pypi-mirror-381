# -*- coding: utf-8 -*-
# Copyright 2025 IRT Saint Exupéry and HECATE European project - All rights reserved
#
# The 2-Clause BSD License
#
# Redistribution and use in source and binary forms, with or without modification, are
# permitted provided that the following conditions are met:
#
# 1. Redistributions of source code must retain the above copyright notice, this list of
#    conditions and the following disclaimer.
#
# 2. Redistributions in binary form must reproduce the above copyright notice, this list
#    of conditions and the following disclaimer in the documentation and/or other
#    materials provided with the distribution.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS “AS IS” AND ANY
# EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF
# MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL
# THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
# SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO,
# PROCUREMENT
# OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
# INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT,
# STRICT
# LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF
# THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
"""
Module for managing and executing co-simulations involving multiple FMUs.

This module provides a `Master` class that handles FMU initialization, input setting,
stepping, and result collection during simulation.

"""
from collections import defaultdict

import numpy as np

from .utils import FixedPointInitializer
from .wrappers import FmuHandlerFactory
import copy


class Master:
    """
    Manages and executes the co-simulation involving multiple FMUs.

    Attributes:
        fmu_config_list (list):
            A list of dictionaries containing information about the FMUs to be used in
            the simulation.
        connections (dict):
            A dictionary of connections between FMUs. The keys are tuples (source_fmu,
            source_variable), and the values are dictionaries with information about the
            source and target FMUs and variables.
        sequence_order (list):
            The order in which FMUs should be executed.
        cosim_method (str):
            The method used to solve algebraic loops in the simulation.
        current_time (float):
            The current simulation time.
        fixed_point (bool):
            Whether to use the fixed-point initialization method.
        fixed_point_kwargs (dict):
            Keyword arguments for the fixed-point initialization method.

    Methods:
        __init__(fmu_config_list, connections, sequence_order, cosim_method="jacobi",
            fixed_point=False, fixed_point_kwargs=None):
            Initializes the Master class with the given FMU list, connection list,
            sequence order, and algebraic loop solver.

        sanity_check():
            Checks FMU compatibility, I/Os, and headers with the corresponding
            algorithm.

        set_inputs(input_dict=None):
            Sets the input values for the current simulation step using the provided
            input dictionary.

        init_simulation(input_dict=None):
            Initializes the simulation environment and FMUs.

        get_outputs() -> dict[str, list]:
            Returns the output dictionary for the current step.

        get_results():
            Returns the results of the simulation.

        solve_loop(fmu_ids, step_size, algo="jacobi"):
            Uses the defined algorithm to solve algebraic loops in the simulation.

        do_step(step_size, input_dict=None, record_outputs=True):
            Performs a single step of the simulation, updating inputs, executing FMUs,
            and propagating outputs.
    """

    # pylint: disable=too-many-instance-attributes

    __keys = {
        "fmus": "FMUs",
        "id": "id",
        "path": "path",
        "init": "initialization",
        "step_t": "steptime",
        "suppl": "supplier",
        "conn": "connections",
        "src_fmu": "source_fmu",
        "src_var": "source_variable",
        "src_unit": "source_unit",
        "tgt_fmu": "target_fmu",
        "tgt_var": "target_variable",
        "tgt_unit": "target_unit",
    }

    def __init__(
        self,
        fmu_config_list: list,
        connections: dict,
        sequence_order: list,
        cosim_method: str = "jacobi",
        iterative: bool = False,
        fixed_point=False,
        fixed_point_kwargs=None,
    ):
        """
        Initializes the Master class with FMU configurations, connection details,
        sequence order, and loop solver.

        Args:
            fmu_config_list (list): List of dictionaries with FMU configurations.
            connections (dict): Dictionary mapping connections between FMUs.
            sequence_order (list): Execution order of FMUs.
            cosim_method (str, optional): Strategy for coordinating FMUs in
                co-simulation. Options are "jacobi" and "gauss-seidel".
                Defaults to "jacobi".
            iterative (str, optional): Whether to solve algebraic loops iteratively.
                Defaults to False.
            fixed_point (bool): whether to use the fixed-point initialization method.
            fixed_point_kwargs (dict): keyword arguments for the fixed point
            initialization
                method if fixed_point is set to True. Defaults to None, in which
                case the default values are used "solver": "fsolve",
                "time_step": minimum_default_step_size, and "xtol": 1e-5.
        """

        self.fmu_config_list = (
            fmu_config_list  # List of FMU configurations (dict) from config file
        )
        self.connections = connections  # Dict of connections between FMUs

        # Cosimulation method (default: Jacobi)
        self.cosim_method = cosim_method
        # Whether iterative method requested (default: False)
        self.iterative = iterative

        # Load FMUs into dict of FMU Handlers
        self.fmu_handlers = self._load_fmus()

        # Check if the names of the variables match between the connection dict and
        # the FMUs
        self._check_connections()

        default_step_sizes = []
        for fmu in self.fmu_handlers.values():
            default_step_sizes.append(fmu.default_step_size)

        ## find the smaller of all step sizes
        # remove None from default_step_sizes
        default_step_sizes = [x for x in default_step_sizes if x is not None]
        if len(default_step_sizes) == 0:
            self.default_step_size = 1.0
        else:
            self.default_step_size = np.min(default_step_sizes)

        # Sequence order of execution as a List of FMU IDs. Extracted by config
        # parser module
        # Sequence order of execution as a List of FMU IDs. Extracted by config parser
        self.sequence_order = sequence_order
        if self.sequence_order is None:
            self.sequence_order = [d[self.__keys["id"]] for d in self.fmu_config_list]

        # init current_time to None to check if init_simulation() has been called
        self.current_time = None
        # Init output and input dictionaries for FMUs to maintain state between steps
        # Initialize arrays for inputs and outputs
        self._input_dict = {
            fmu_id: np.zeros(len(fmu.get_input_names()))
            for fmu_id, fmu in self.fmu_handlers.items()
        }

        self._output_dict = {
            fmu_id: np.zeros(len(fmu.get_output_names()))
            for fmu_id, fmu in self.fmu_handlers.items()
        }
        # Results dictionary to store the output values for each step
        self._results = defaultdict(list)

        self.fixed_point = fixed_point
        self.fixed_point_kwargs = fixed_point_kwargs

        if fixed_point and fixed_point_kwargs is None:
            self.fixed_point_kwargs = {
                "solver": "fsolve",
                "time_step": self.default_step_size,
                "xtol": 1e-5,
            }

        # self.init_simulation(fixed_point=False)

    def sanity_check(self):  # TODO
        """
        Checks the compatibility of FMUs, including input/output validation and
        algorithm compliance.
        """
        self._check_connections()

    def _check_connections(self):
        """
        Checks whether the variable names in connections match the actual
        variable names in the FMUs and verifies that the source variable is an 'output'
        and the target variable is an 'input' (if causality is specified).

        Raises:
            ValueError: If a variable name does not exist in the respective FMU.
            ValueError: If the source variable is not an 'output' or the target variable
                is not an 'input'.
        """
        for (source_fmu, source_var), targets in self.connections.items():

            # Check if source variable exists in source FMU output list
            if source_var not in self.fmu_handlers[source_fmu].get_output_names():
                raise ValueError(
                    f"Source variable '{source_var}' not found in outputs of "
                    f"FMU '{source_fmu}': "
                    f"{self.fmu_handlers[source_fmu].get_output_names()}"
                )

            for target_fmu, target_var in targets:
                # Check if target variable exists in target FMU input list
                if target_var not in self.fmu_handlers[target_fmu].get_input_names():
                    raise ValueError(
                        f"Target variable '{target_var}' not found in inputs of "
                        f"FMU '{target_fmu}': "
                        f"{self.fmu_handlers[target_fmu].get_input_names()}"
                    )

    def _load_fmus(self, id_key="id", path_key="path"):
        """Loads FMU Handlers and stores them in a dictionary. This method also check
            if fmus are ready to make cosimulation :
            - Cosimulation mode (not ModelExchange)
            - Can Get and Set States (for loop solver iterations)

        Args:
            id_key (str): Key for FMU IDs (default: "id").
            path_key (str): Key for FMU paths (default: "path").

        Returns:
            Dictionary of FMU Handlers.
        """
        fmu_handlers = {}
        for fmu_info_dict in self.fmu_config_list:
            # Load FMU (custom handler from wrappers)
            fmu_path = fmu_info_dict[path_key]

            # Store it into fmus dictionary
            fmu_handlers[fmu_info_dict[id_key]] = FmuHandlerFactory(fmu_path)()

            # Check fmu parameters are correct for cosimulation
            # Check Cosimulation mode
            model_description = fmu_handlers[fmu_info_dict[id_key]].description
            if model_description.coSimulation is None:
                raise Exception(f"Fmu {fmu_path} is not in co-simulation mode.")
            # if iterative algorithm requested, check fmus are able to set/get states
            if self.iterative and (
                not model_description.coSimulation.canGetAndSetFMUstate
            ):
                raise Exception(
                    f"Can't get or set States on fmu {fmu_path} but it is "
                    f"required for iterative solvers."
                )

        return fmu_handlers

    def initialize_values_from_config(self):
        """
        Initializes the FMU variables (inputs/outputs/parameters) with the values
        provided in the configuration dict.

        If the variable is an input, it is also added to the input dictionary
        """
        if self.current_time is None:
            raise RuntimeError(
                "Current time is not initialized. Call init_simulation() first."
            )

        for fmu in self.fmu_config_list:
            fmu_handler = self.fmu_handlers[fmu[self.__keys["id"]]]
            for key, value in fmu[self.__keys["init"]].items():
                fmu_handler.set_variables({key: [value]})
                if key in fmu_handler.get_input_names():
                    self._input_dict[fmu[self.__keys["id"]]][key] = [value]

    def set_inputs(self, input_dict=None):
        """
        Sets the input values for the current simulation step.

        This method populates the internal input dictionary (`self._input_dict`) with
        values for the current step. It updates these values with those provided in the
        `input_dict` parameter, if given. The `input_dict` parameter is expected to be
        a dictionary of dictionaries, where each key is an FMU identifier and each value
        is another dictionary mapping variable names to their respective values (e.g.,
        {"FMU1": {"var1": value}, "FMU2": {"var2": val, "var3": val}}).

        Args:
            input_dict (dict, optional): A dictionary of dictionaries containing input
                values to override the initialization values. Defaults to None.

        Raises:
            RuntimeError: If the current simulation time (`self.current_time`) is not
                initialized. Ensure that init_simulation()` is called before invoking
                this method.
        """
        if self.current_time is None:
            raise RuntimeError(
                "Current time is not initialized. Call init_simulation() first."
            )

        if input_dict:  # True if input_dict is not empty
            for fmu in input_dict:
                if fmu not in self.fmu_handlers:
                    raise ValueError(
                        f"FMU '{fmu}' not found in FMUs: "
                        f"{list(self.fmu_handlers.keys())}."
                    )
                for variable in input_dict[fmu]:
                    if (
                        variable
                        not in self.fmu_handlers[fmu].get_input_names()
                        + self.fmu_handlers[fmu].get_parameter_names()
                    ):
                        raise ValueError(
                            f"Variable '{variable}' not found in inputs of FMU '{fmu}':"
                            f" {self.fmu_handlers[fmu].get_input_names()}."
                        )
                    # Set given values (will overide values set previously in init)
                    self._input_dict[fmu][variable] = input_dict[fmu][variable]

    def get_input_dict(self) -> dict:
        """
        Returns the input dictionary for the current step.

        Returns:
            dict: A dictionary containing the input values for the current step,
                structured as `[fmu_id][variable_name] => list(value)`.
        """
        return self._input_dict

    def init_simulation(self, input_dict=None):
        """
        Initializes the simulation environment and FMUs.

        This method sets up the necessary dictionaries for the simulation and
        initializes the FMUs with either a fixed point algorithm or values provided in
        the input dictionary.

        Args:
            input_dict (dict): A dictionary containing input values for the simulation.
                Defaults to None.

        The method performs the following steps:
            1. Sets the current simulation time to 0.
            2. If fixed_point is True, calls the _fixed_point_init() method.
            3. Otherwise, sets the inputs using the provided input_dict and initializes
                each FMU with these values.

        **Note**: The FMUs are reset after setting the initial values.
        """

        # # Init output and input dictionaries
        for fmu_id, fmu in self.fmu_handlers.items():
            self._output_dict[fmu_id] = {key: [0] for key in fmu.get_output_names()}
            self._input_dict[fmu_id] = {key: [0] for key in fmu.get_input_names()}

        # Init current_time of simulation to 0
        self.current_time = 0.0

        # Init input/output/parameter variables with the values provided in the config
        self.initialize_values_from_config()

        # INIT: call fixed_step()
        if self.fixed_point:
            print("Calling Fixed Point Initialization")
            self.set_inputs(input_dict=input_dict)
            fixed_point_solver = FixedPointInitializer(self, **self.fixed_point_kwargs)
            fixed_point_solution = fixed_point_solver.solve()
            self.set_inputs(input_dict=fixed_point_solution)
        else:
            print("Skipping Fixed Point Initialization")
            self.set_inputs(input_dict=input_dict)

        for fmu_id, fmu_handler in self.fmu_handlers.items():
            init_dict = self._input_dict[fmu_id]
            fmu_handler.set_variables(init_dict)
            fmu_handler.reset()

    def get_outputs(self) -> dict[str, list]:
        """
        Returns the output dictionary for the current step.

        Returns:
            dict: A dictionary containing the output values of the current step,
                structured as `[FMU_ID][Var]`.
        """
        return self._output_dict

    def get_results(self) -> dict:
        """
        Returns the results of the simulation, this includes the values of every output
        variables, for each step, up until the current time of simulation.

        Returns:
            dict: A dictionnary containing output values of every step, structured as
                [(FMU_ID, Var)]

        """
        return self._results

    def solve_loop(
        self, fmu_ids, step_size: float, algo="jacobi", iterative=False
    ) -> dict:
        """
        Performs a single simulation step on the given FMUs, using the defined algorithm
        to solve algebraic loops in the simulation.

        In the case there is no loop, the function will propagate the output values and
        return them.

        Args:
            fmu_ids (list[str]): List of highly coupled FMUs. Contains only one FMU if
                there is no loop.
            step_size (float): The step size for **data exchange** (in cosimulation
                mode, FMU integration step is fixed).
            algo (str): The algorithm to use to solve the loop (default: "jacobi").
            iterative (bool): Whether iterative method requested to solve the loop.

        Returns:
            dict: A dictionary containing the output values for this step of the FMUs
                given, structured as `[FMU_ID][Var]`

        """

        # Verify algo is a known algo name
        if algo not in ("jacobi", "gauss_seidel"):
            raise NotImplementedError(
                f"Algorithm {algo} not implemented for loop solving."
            )

        output = {}  # key: fmu_id, value: output_dict (var_name, value)
        inputs = {}
        current_iteration = 0
        tol = 1e-3
        max_iteration = 10
        converged = False
        first_iteration = True
        fmu_states = defaultdict(list)  # variable for state storage for each FMU

        while not converged and current_iteration < max_iteration:
            for fmu_id in fmu_ids:
                fmu = self.fmu_handlers[fmu_id]

                if iterative:
                    if first_iteration:  # If first time => save state
                        fmu_states[fmu_id] = fmu.get_state()
                    else:  # If not first time => retrieve state
                        fmu.set_state(fmu_states[fmu_id])  # TODO : is exists state ?

                # Save inputs for check coherence
                inputs[fmu_id] = copy.deepcopy(self._input_dict[fmu_id])
                output[fmu_id] = fmu.step(
                    self.current_time, step_size, self._input_dict[fmu_id]
                )

                # Update inputs, only for gauss-seidel algo
                if algo == "gauss_seidel":
                    self.apply_fmu_outputs_to_inputs(fmu_id, output[fmu_id])

            # Exit loop if not iterative or only 1 FMU inside loop
            if not iterative or len(fmu_ids) == 1:
                break

            conv_val = True
            residuals = self.get_residual(inputs, output)
            for fmu_id, residual in residuals.items():
                conv_val = conv_val and residual < tol

            converged = conv_val
            first_iteration = False
            current_iteration += 1

        """
        if iterative and len(fmu_ids) != 1:
            if current_iteration == max_iteration:
                print(
                    str(self.current_time)
                    + " - Max iteration reached with following solution "
                    + str(output)
                )
            else:
                print(
                    str(self.current_time)
                    + " - Convergence found "
                    + str(current_iteration)
                    + " iterations"
                )
        """
        return output

    def do_fixed_point_step(self, step_size: float, input_dict=None):
        """
        This method updates the input dictionary with the values from the provided input
        dictionary, performs a single step of the simulation on each FMU, using the
        default jacobi method, propagates the output values to the corresponding
        variables for the next step, and updates the current simulation time accordingly. It also
        stores the output values in the results dictionary.

        Args:
            step_size (float): The size of the simulation step.
            input_dict (dict, optional): A dictionary containing input values for the
                simulation. Defaults to None.
            record_outputs (bool, optional): Whether to store the output values in the
                results dictionary. Defaults to True.

        Returns:
            dict: A dictionary containing the output values for this step, structured as
                `[FMU_ID][Var]`.

        """
        self.set_inputs(input_dict=input_dict)
        for fmu_ids in self.sequence_order:
            # out is fill with key: fmu_id, value: output_dict (var_name, value)
            out = self.solve_loop(fmu_ids, step_size)

            for fmu_id, fmu_output_dict in out.items():
                for output_name, value in fmu_output_dict.items():

                    # add each output to the output dict, [FMU_ID][Var] as key
                    self._output_dict[fmu_id][output_name] = value

        # update 1 for all inputs with outputs
        for fmu_id, fmu_output_dict in self._output_dict.items():
            self.apply_fmu_outputs_to_inputs(fmu_id, fmu_output_dict)
        self.current_time += step_size
        # Return the output value for this step
        return self._output_dict

    def do_step(self, step_size: float, input_dict=None, record_outputs=True) -> dict:
        """
        This method updates the input dictionary with the values from the provided input
        dictionary, performs a single step of the simulation on each FMU, using the
        solve_loop method, propagates the output values to the corresponding variables
        for the next step, and updates the current simulation time accordingly. It also
        stores the output values in the results dictionary.

        Args:
            step_size (float): The size of the simulation step.
            input_dict (dict, optional): A dictionary containing input values for the
                simulation. Defaults to None.
            record_outputs (bool, optional): Whether to store the output values in the
                results dictionary. Defaults to True.

        Returns:
            dict: A dictionary containing the output values for this step, structured as
                `[FMU_ID][Var]`.

        """
        self.set_inputs(input_dict=input_dict)
        for fmu_ids in self.sequence_order:
            # out is fill with key: fmu_id, value: output_dict (var_name, value)
            out = self.solve_loop(
                fmu_ids, step_size, algo=self.cosim_method, iterative=self.iterative
            )

            for fmu_id, fmu_output_dict in out.items():
                for output_name, value in fmu_output_dict.items():
                    if self.cosim_method == "gauss_seidel":
                        # Update inputs connected to FMU outputs
                        self.update_connected_inputs(fmu_id, output_name, value)

                    if record_outputs:
                        # add each output to the result dict, (FMU_ID + Var) as key
                        self._results[(fmu_id, output_name)].extend(value)

                    # add each output to the output dict, [FMU_ID][Var] as key
                    self._output_dict[fmu_id][output_name] = value

        # If jacobi, update 1 for all inputs with outputs
        if self.cosim_method == "jacobi":
            for fmu_id, fmu_output_dict in self._output_dict.items():
                self.apply_fmu_outputs_to_inputs(fmu_id, fmu_output_dict)
        if record_outputs:
            self._results["time"].append(self.current_time)
        self.current_time += step_size
        # Return the output value for this step
        return self._output_dict

    def get_residual(self, input_dict: dict, output_dict: dict):
        """
        Performs check between outputs and connected inputs and return a list of
        residuals
        The check is based on connections between given fmu/outputs and inpout dict for
        each FMU.

        Args:
            output_dict: A dictionary containing the output values for the current step
            input_dict: Input dict concerned by the check, transient dict with current
                calculated values

        Returns:
            residuals: A list of residuals between inputs and outputs
                (1 for each connection)
        """
        residuals = {}
        for fmu_id, out_fmu in output_dict.items():
            for output_name, value in out_fmu.items():
                if (fmu_id, output_name) in self.connections:
                    for target_fmu, target_variable in self.connections[
                        (fmu_id, output_name)
                    ]:
                        residuals[target_fmu + "_" + target_variable] = np.abs(
                            input_dict[target_fmu][target_variable][0] - value[0]
                        )

        return residuals

    def apply_fmu_outputs_to_inputs(self, fmu_id: str, out_fmu: dict):
        """
        Performs a copy of output values into input dict.
        The copy is based on connections between given fmu/outputs and inpout dict for
        each FMU.

        Args:
            out_fmu: A dictionary containing the output values for the current step
                on a given fmu, identified by fmu_id
            fmu_id: A String identifying FMU into system. Used to find connections with
                outputs

        Returns:
            No return, at the end of the method, self._input_dict is fill with updated
                values.
        """
        for output_name, value in out_fmu.items():
            self.update_connected_inputs(fmu_id, output_name, value)

    def update_connected_inputs(self, fmu_id: str, output_name: str, value):
        """
        Performs a copy of output value into input dict.
        The copy is based on connections between given fmu/output name and inpout dict
        for each connected FMU.

        Args:
            fmu_id: A String identifying FMU into system. Used to find connections
                between inputs and output
            output_name: A string that identifies name of the output. Used to find
                connections with inputs
            value: the value to copy to inputs

        Returns:
            No return, at the end of the method, self._input_dict is fill with updated
                value.
        """
        # If output is connected, transfer the value to the connected FMU(s)
        if (fmu_id, output_name) in self.connections:
            for target_fmu, target_variable in self.connections[(fmu_id, output_name)]:
                self._input_dict[target_fmu][target_variable] = value
