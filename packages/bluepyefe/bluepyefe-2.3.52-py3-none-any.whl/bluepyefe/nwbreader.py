import logging
import numpy

logger = logging.getLogger(__name__)

PROTOCOL_VU_TO_BBP = {
    "X1PS_SubThresh_DA_0": "IV",
    "X2LP_Search_DA_0": "IDthresh",
    "X4PS_SupraThresh_DA_0": "IDrest",
    "CCSteps_DA_0": "Step"
}


class NWBReader:
    def __init__(self, content, target_protocols, repetition=None, v_file=None):
        """ Init

        Args:
            content (h5.File): NWB file
            target_protocols (list of str): list of the protocols to be read and returned
            repetition (list of int): id of the repetition(s) to be read and returned
            v_file (str): name of original file that can be retrieved in sweep's description
        """

        self.content = content
        self.target_protocols = target_protocols
        self.repetition = repetition
        self.v_file = v_file

    def read(self):
        """ Read the content of the NWB file

        Returns:
            data (list of dict): list of traces"""

        raise NotImplementedError()

    def _format_nwb_trace(self, voltage, current, start_time, trace_name=None, repetition=None):
        """ Format the data from the NWB file to the format used by BluePyEfe

        Args:
            voltage (Dataset): voltage series
            current (Dataset): current series
            start_time (Dataset): starting time
            trace_name (Dataset): name of the trace
            repetition (int): repetition number

        Returns:
            dict: formatted trace
        """
        v_array = numpy.array(
            voltage[()] * voltage.attrs["conversion"], dtype="float32"
        )

        i_array = numpy.array(
            current[()] * current.attrs["conversion"], dtype="float32"
        )

        dt = 1. / float(start_time.attrs["rate"])

        v_unit = voltage.attrs["unit"]
        i_unit = current.attrs["unit"]
        t_unit = start_time.attrs["unit"]
        if not isinstance(v_unit, str):
            v_unit = voltage.attrs["unit"].decode('UTF-8')
            i_unit = current.attrs["unit"].decode('UTF-8')
            t_unit = start_time.attrs["unit"].decode('UTF-8')

        return {
            "voltage": v_array,
            "current": i_array,
            "dt": dt,
            "id": str(trace_name),
            "repetition": repetition,
            "i_unit": i_unit,
            "v_unit": v_unit,
            "t_unit": t_unit,
        }


class AIBSNWBReader(NWBReader):
    def read(self):
        """ Read the content of the NWB file

        Returns:
            data (list of dict): list of traces"""

        data = []

        for sweep in list(self.content["acquisition"]["timeseries"].keys()):
            protocol_name = self.content["acquisition"]["timeseries"][sweep]["aibs_stimulus_name"][()]
            if not isinstance(protocol_name, str):
                protocol_name = protocol_name.decode('UTF-8')

            if (
                self.target_protocols and
                protocol_name.lower() not in [prot.lower() for prot in self.target_protocols]
            ):
                continue

            data.append(self._format_nwb_trace(
                voltage=self.content["acquisition"]["timeseries"][sweep]["data"],
                current=self.content["stimulus"]["presentation"][sweep]["data"],
                start_time=self.content["acquisition"]["timeseries"][sweep]["starting_time"],
                trace_name=sweep
            ))

        return data


class ScalaNWBReader(NWBReader):

    def read(self):
        """ Read and format the content of the NWB file

        Returns:
            data (list of dict): list of traces
        """

        data = []

        if self.repetition:
            repetitions_content = self.content['general']['intracellular_ephys']['intracellular_recordings']['repetition']
            if isinstance(self.repetition, (int, str)):
                self.repetition = [int(self.repetition)]

        for sweep in list(self.content['acquisition'].keys()):
            key_current = sweep.replace('Series', 'StimulusSeries')
            try:
                protocol_name = self.content["acquisition"][sweep].attrs["stimulus_description"]
            except KeyError:
                logger.warning(f'Could not find "stimulus_description" attribute for {sweep}, Setting it as "Step"')
                protocol_name = "Step"

            if ("na" == protocol_name.lower()) or ("step" in protocol_name.lower() and "genericstep" != protocol_name.lower()):
                protocol_name = "Step"

            if (
                self.target_protocols and
                protocol_name.lower() not in [prot.lower() for prot in self.target_protocols]
            ):
                continue

            if key_current not in self.content['stimulus']['presentation']:
                continue

            if self.repetition:
                sweep_id = int(sweep.split("_")[-1])
                if (int(repetitions_content[sweep_id]) in self.repetition):
                    data.append(self._format_nwb_trace(
                        voltage=self.content['acquisition'][sweep]['data'],
                        current=self.content['stimulus']['presentation'][key_current]['data'],
                        start_time=self.content['acquisition'][sweep]["starting_time"],
                        trace_name=sweep,
                        repetition=int(repetitions_content[sweep_id])
                    ))
            else:
                data.append(self._format_nwb_trace(
                    voltage=self.content['acquisition'][sweep]['data'],
                    current=self.content['stimulus']['presentation'][key_current]['data'],
                    start_time=self.content["acquisition"][sweep]["starting_time"],
                    trace_name=sweep,
                ))

        return data


class BBPNWBReader(NWBReader):
    def _get_repetition_keys_nwb(self, ecode_content, request_repetitions=None):
        """ Filter the names of the traces based on the requested repetitions

        Args:
            ecode_content (dict): content of the NWB file for one eCode/protocol
            request_repetitions (list of int): identifier of the requested repetitions

        Returns:
            list of str: list of the keys of the traces to be read
        """

        if isinstance(request_repetitions, (int, str)):
            request_repetitions = [int(request_repetitions)]

        reps = list(ecode_content.keys())
        reps_id = [int(rep.replace("repetition ", "")) for rep in reps]

        if request_repetitions:
            return [reps[reps_id.index(i)] for i in request_repetitions]
        else:
            return list(ecode_content.keys())

    def read(self):
        """ Read and format the content of the NWB file

        Returns:
            data (list of dict): list of traces
        """

        data = []

        for ecode in self.target_protocols:
            for cell_id in self.content["data_organization"].keys():
                if ecode not in self.content["data_organization"][cell_id]:
                    new_ecode = next(
                        iter(
                            ec
                            for ec in self.content["data_organization"][cell_id]
                            if ec.lower() == ecode.lower()
                        ),
                        None
                    )
                    if new_ecode:
                        logger.debug(
                            f"Could not find {ecode} in nwb file, will use {new_ecode} instead"
                        )
                        ecode = new_ecode
                    else:
                        logger.debug(f"No eCode {ecode} in nwb.")
                        continue

                ecode_content = self.content["data_organization"][cell_id][ecode]

                rep_iter = self._get_repetition_keys_nwb(
                    ecode_content, request_repetitions=self.repetition
                )

                for rep in rep_iter:
                    for sweep in ecode_content[rep].keys():
                        for trace_name in list(ecode_content[rep][sweep].keys()):
                            if "ccs_" in trace_name:
                                key_current = trace_name.replace("ccs_", "ccss_")
                            elif "ic_" in trace_name:
                                key_current = trace_name.replace("ic_", "ics_")
                            else:
                                continue

                            if key_current not in self.content["stimulus"]["presentation"]:
                                logger.debug(f"Ignoring {key_current} not"
                                             " present in the stimulus presentation")
                                continue

                            if trace_name not in self.content["acquisition"]:
                                logger.debug(f"Ignoring {trace_name} not"
                                             " present in the acquisition")
                                continue

                            # if we have v_file, check that trace comes from this original file
                            if self.v_file is not None:
                                attrs = self.content["acquisition"][trace_name].attrs
                                if "description" not in attrs:
                                    logger.warning(
                                        "Ignoring %s because no description could be found.",
                                        trace_name
                                    )
                                    continue
                                v_file_end = self.v_file.split("/")[-1]
                                if v_file_end != attrs.get("description", "").split("/")[-1]:
                                    logger.debug(f"Ignoring {trace_name} not matching v_file")
                                    continue

                            data.append(self._format_nwb_trace(
                                voltage=self.content["acquisition"][trace_name]["data"],
                                current=self.content["stimulus"]["presentation"][key_current][
                                    "data"],
                                start_time=self.content["stimulus"]["presentation"][key_current][
                                    "starting_time"],
                                trace_name=trace_name,
                                repetition=int(rep.replace("repetition ", ""))
                            ))

        return data


class TRTNWBReader(NWBReader):
    """Read NWB files used in 'An in vitro whole-cell electrophysiology dataset of
    human cortical neurons' by Howard, Derek et al., 2022, doi.org/10.1093/gigascience/giac108.
    The files that can be read by this reader can be found at
    10.48324/dandi.000293/0.220708.1652 (human), and
    10.48324/dandi.000292/0.220708.1652 (mouse).
    """

    def read(self):
        """ Read and format the content of the NWB file
        Returns:
            data (list of dict): list of traces
        """
        data = []

        # Only return data if target_protocols is None or includes "step" or "genericstep"
        if self.target_protocols:
            allowed = [p.lower() for p in self.target_protocols]
            if "step" not in allowed and "genericstep" not in allowed:
                logger.warning(
                    "TRTNWBReader only supports 'step' and 'genericstep' protocols, "
                    f"but requested: {self.target_protocols}. Skipping."
                )
                return []

        # possible paths in content:
        # /acquisition/index_00
        # or /acquisition/index_000
        # or /acquisition/Index_0_0_0
        for voltage_sweep_name, voltage_sweep in list(self.content["acquisition"].items()):
            parts = voltage_sweep_name.split("_")
            if len(parts) == 2:
                # maps 00 -> 01, 01 -> 03, ... or 000 -> 001, etc.
                str_size = len(parts[-1])
                parts[-1] = str(2 * int(parts[-1]) + 1).rjust(str_size, "0")
            else:
                # maps 0_0_0 -> 0_0_1, 0_0_1 -> 0_0_0, etc.
                if parts[-1] == "0":
                    parts[-1] = "1"
                elif parts[-1] == "1":
                    parts[-1] = "0"
                elif parts[-1] == "2":
                    parts[-1] = "3"
                elif parts[-1] == "3":
                    parts[-1] = "2"

            current_sweep_name = "_".join(parts)
            # possible paths in content:
            # /stimulus/presentation/index_01
            # or /stimulus/presentation/index_001
            # or /stimulus/presentation/Index_0_0_1
            current_sweep = self.content["stimulus"]["presentation"][current_sweep_name]

            data.append(self._format_nwb_trace(
                voltage=voltage_sweep["data"],
                current=current_sweep["data"],
                start_time=voltage_sweep["starting_time"],
                trace_name=voltage_sweep_name
            ))

        return data

    def _format_nwb_trace(self, voltage, current, start_time, trace_name=None, repetition=None):
        """ Format the data from the NWB file to the format used by BluePyEfe

        Args:
            voltage (Dataset): voltage series
            current (Dataset): current series
            start_time (Dataset): starting time
            trace_name (Dataset): name of the trace
            repetition (int): repetition number

        Returns:
            dict: formatted trace
        """
        v_conversion = voltage.attrs["conversion"]
        i_conversion = current.attrs["conversion"]
        v_unit = voltage.attrs["unit"]
        i_unit = current.attrs["unit"]
        t_unit = start_time.attrs["unit"]
        if not isinstance(v_unit, str):
            v_unit = voltage.attrs["unit"].decode('UTF-8')
            i_unit = current.attrs["unit"].decode('UTF-8')
            t_unit = start_time.attrs["unit"].decode('UTF-8')

        if (
            v_conversion == 1e-12 and
            i_conversion == 0.001 and
            v_unit == "volts" and
            i_unit == "volts"
        ):
            # big mixup in units, correct it
            v_conversion = 1e-3
            i_conversion = 1e-12
            i_unit = "amperes"

        v_array = numpy.array(
            voltage[()] * v_conversion, dtype="float32"
        )

        i_array = numpy.array(
            current[()] * i_conversion, dtype="float32"
        )

        dt = 1. / float(start_time.attrs["rate"])

        return {
            "voltage": v_array,
            "current": i_array,
            "dt": dt,
            "id": str(trace_name),
            "repetition": repetition,
            "i_unit": i_unit,
            "v_unit": v_unit,
            "t_unit": t_unit,
        }


class VUNWBReader(NWBReader):

    def __init__(self, content, target_protocols, in_data, repetition=None):
        """ Init
        Args:
            content (h5.File): NWB file
            target_protocols (list of str): list of the protocols to be read and returned
            repetition (list of int): id of the repetition(s) to be read and returned
        """

        self.content = content
        self.target_protocols = target_protocols
        self.repetition = repetition
        self.in_data = in_data

    def read(self):
        """ Read and format the content of the NWB file
        Returns:
            data (list of dict): list of traces
        """

        data = []
        for sweep_name, current_sweep in list(self.content["stimulus"]["presentation"].items()):

            stimulus_description = None
            try:
                stimulus_description = current_sweep.attrs["stimulus_description"]
            except KeyError:
                stimulus_description = current_sweep["stimulus_description"][()][0].decode('UTF-8')

            if stimulus_description not in PROTOCOL_VU_TO_BBP:
                continue
            translated_name = PROTOCOL_VU_TO_BBP[stimulus_description]

            if translated_name != self.in_data["protocol_name"]:
                continue

            voltage_sweep_name = sweep_name.replace("DA", "AD")

            voltage_sweeps = self.content["acquisition"]["timeseries"] if "timeseries" in self.content["acquisition"] else self.content["acquisition"]

            if voltage_sweep_name not in voltage_sweeps:
                continue
            data.append(self._format_nwb_trace(
                voltage=voltage_sweeps[voltage_sweep_name]["data"],
                current=current_sweep["data"],
                start_time=voltage_sweeps[voltage_sweep_name]["starting_time"],
                trace_name=sweep_name
            ))

            # Shorten protocols that finish with NaNs
            first_nan = numpy.argmax(numpy.isnan(data[-1]["current"]))
            if first_nan:
                data[-1]["voltage"] = data[-1]["voltage"][:first_nan]
                data[-1]["current"] = data[-1]["current"][:first_nan]

            # Remove the protocols that finish too early
            if "toff" in self.in_data and self.in_data["toff"] > len(data[-1]["current"]) * data[-1]["dt"] * 1000:
                data.pop(-1)
            else:
                # Offset the current with the holding current
                holding_current = float(voltage_sweeps[voltage_sweep_name]["bias_current"][()]) * 1e-12  # in pA
                data[-1]["current"] = numpy.asarray(data[-1]["current"]) + holding_current

            # For Step, IV and IDRest protocols, replace the first 90 ms with the value at 90 ms
            # if stimulus_description == "CCSteps_DA_0":
            if any(stimulus_description in s for s in ["CCSteps_DA_0", "X1PS_SubThresh_DA_0", "X4PS_SupraThresh_DA_0"]):
                if int(0.090 / data[-1]["dt"]) < len(data[-1]["current"]):
                    data[-1]["current"][0:int(0.090 / data[-1]["dt"])] = data[-1]["current"][int(0.090 / data[-1]["dt"])]
                    data[-1]["voltage"][0:int(0.090 / data[-1]["dt"])] = data[-1]["voltage"][int(0.090 / data[-1]["dt"])]
                else:
                    # Handle the case when the index is out of bounds
                    # You can choose to raise an exception, set a default value, or handle it in a different way
                    logger.info(f"For {stimulus_description}, unable to replace 0-40 ms value with the one at 40th ms as current/voltage array is too short")
                    continue

        return data
