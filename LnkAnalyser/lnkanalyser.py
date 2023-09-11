from datetime import timedelta, datetime
import pprint

def convert_to_readable_date(hex_timestamp):
    # number of nanoseconds since january 1st, 1601
    nanoseconds_since_microsoft_epoch = int(hex_timestamp, 16) * 100
    days_since_microsoft_epoch = nanoseconds_since_microsoft_epoch / 8.64e13
    timestamp_of_target = datetime(1601, 1, 1, 0, 0, 0) + timedelta(days=days_since_microsoft_epoch)
    return timestamp_of_target


counters = {
    "bytes": 0
}


def increment_byte_counter():
    counters["bytes"] = counters["bytes"] + 1


def get_byte_counter():
    return counters["bytes"]


def go(path, endian="little"):
    """Given a path to a Windows shortcut, return a dict() containing the properties of the shortcut

    :param path: The path of the Windows shortcut to load
    :param endian: Determine the endian order of the bytes in the output. You may prefer to use "little" to keep it
    consistent with the Windows standard.
    :return :dict: A dictionary containing the parsed properties of the Windows shortcut, in big endian format by
    default
    """
    properties = dict()

    """
    Notes
    * Multi-byte data values in the LNK format are stored in little-endian format.
    """
    with open(path, "rb") as lnk_file:
        properties["header_size"] = list()
        properties["link_class_id"] = list()
        properties["link_flags"] = list()
        properties["file_attributes"] = list()
        properties["creation_time_of_link_target"] = list()
        properties["access_time_of_link_target"] = list()
        properties["write_time_of_link_target"] = list()
        properties["target_file_size"] = list()
        properties["icon_index"] = list()
        properties["expected_window_state"] = list()
        properties["hot_key"] = list()
        properties["reserved_one"] = list()
        properties["reserved_two"] = list()
        properties["reserved_three"] = list()

        while byte := lnk_file.read(1).hex():

            if 0 <= get_byte_counter() < 4:
                properties["header_size"].append(byte)

            if 4 <= get_byte_counter() < 20:
                properties["link_class_id"].append(byte)

            if 20 <= get_byte_counter() < 24:
                properties["link_flags"].append(byte)

            if 24 <= get_byte_counter() < 28:
                properties["file_attributes"].append(byte)

            if 28 <= get_byte_counter() < 36:
                properties["creation_time_of_link_target"].append(byte)

            if 36 <= get_byte_counter() < 44:
                properties["access_time_of_link_target"].append(byte)

            if 44 <= get_byte_counter() < 52:
                properties["write_time_of_link_target"].append(byte)

            if 52 <= get_byte_counter() < 56:
                properties["target_file_size"].append(byte)

            if 56 <= get_byte_counter() < 60:
                properties["icon_index"].append(byte)

            if 60 <= get_byte_counter() < 64:
                properties["expected_window_state"].append(byte)

            if 64 <= get_byte_counter() < 66:
                properties["hot_key"].append(byte)

            if 66 <= get_byte_counter() < 68:
                properties["reserved_one"].append(byte)

            if 68 <= get_byte_counter() < 72:
                properties["reserved_two"].append(byte)

            if 72 <= get_byte_counter() < 76:
                properties["reserved_three"].append(byte)

            increment_byte_counter()

        if endian == "big":
            for key, value in properties.items():
                value.reverse()

    pprint.pprint(parseLinkHeaderFlags(properties["link_flags"]))

    return properties


def parseLinkHeaderFlags(link_flags):
    byte_data = bytes.fromhex(''.join(link_flags))

    link_header_flags = dict()

    link_header_flags["has_link_target_id_list"] = bool(byte_data[0] & (1 << 0) != 0)
    link_header_flags["has_link_info"] = bool(byte_data[0] & (1 << 1) != 0)
    link_header_flags["has_name"] = bool(byte_data[0] & (1 << 2) != 0)
    link_header_flags["has_relative_path"] = bool(byte_data[0] & (1 << 3) != 0)
    link_header_flags["has_working_dir"] = bool(byte_data[0] & (1 << 4) != 0)
    link_header_flags["has_arguments"] = bool(byte_data[0] & (1 << 5) != 0)
    link_header_flags["has_icon_location"] = bool(byte_data[0] & (1 << 6) != 0)
    link_header_flags["is_unicode"] = bool(byte_data[0] & (1 << 7) != 0)

    link_header_flags["force_no_link_info"] = bool(byte_data[0] & (1 << 8) != 0)
    link_header_flags["has_exp_string"] = bool(byte_data[0] & (1 << 9) != 0)
    link_header_flags["run_in_separate_process"] = bool(byte_data[0] & (1 << 10) != 0)
    link_header_flags["unused_1"] = bool(byte_data[0] & (1 << 11) != 0)
    link_header_flags["has_drawin_id"] = bool(byte_data[0] & (1 << 12) != 0)
    link_header_flags["run_as_user"] = bool(byte_data[0] & (1 << 13) != 0)
    link_header_flags["has_exp_icon"] = bool(byte_data[0] & (1 << 14) != 0)
    link_header_flags["no_pidl_alias"] = bool(byte_data[0] & (1 << 15) != 0)

    link_header_flags["unused_2"] = bool(byte_data[0] & (1 << 16) != 0)
    link_header_flags["run_with_shim_layer"] = bool(byte_data[0] & (1 << 17) != 0)
    link_header_flags["force_no_link_track"] = bool(byte_data[0] & (1 << 18) != 0)
    link_header_flags["enable_target_metadata"] = bool(byte_data[0] & (1 << 19) != 0)
    link_header_flags["disable_link_path_tracking"] = bool(byte_data[0] & (1 << 20) != 0)
    link_header_flags["disable_known_folder_tracking"] = bool(byte_data[0] & (1 << 21) != 0)
    link_header_flags["disable_known_folder_alias"] = bool(byte_data[0] & (1 << 22) != 0)
    link_header_flags["allow_link_to_link"] = bool(byte_data[0] & (1 << 23) != 0)

    link_header_flags["unalias_on_save"] = bool(byte_data[0] & (1 << 24) != 0)
    link_header_flags["prefer_environment_path"] = bool(byte_data[0] & (1 << 25) != 0)
    link_header_flags["keep_local_id_list_for_unc_target"] = bool(byte_data[0] & (1 << 26) != 0)
    link_header_flags["bit_27"] = bool(byte_data[0] & (1 << 27) != 0)
    link_header_flags["bit_28"] = bool(byte_data[0] & (1 << 28) != 0)
    link_header_flags["bit_29"] = bool(byte_data[0] & (1 << 29) != 0)
    link_header_flags["bit_30"] = bool(byte_data[0] & (1 << 30) != 0)
    link_header_flags["bit_31"] = bool(byte_data[0] & (1 << 31) != 0)

    return link_header_flags

