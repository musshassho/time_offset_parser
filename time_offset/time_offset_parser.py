import os
import json
import nuke
import re
import pprint


#CONSTANTS
PATH = "C:\logs"

#FUNCTIONS

def find_upstream_reads(nd_input):
    """
    :param nd_input:
    :return:
    """
    read_node_list = []
    for i_input_idx in range(nd_input.inputs()):
        if nd_input.input(i_input_idx).Class() == "Read":
            read_node_list.append(nd_input.input(i_input_idx))
        else:
            find_upstream_reads(nd_input.input(i_input_idx))
    return read_node_list


def get_retime_():

    retime_nodes = nuke.allNodes("Retime")
    script_first_frame = int(nuke.root()['first_frame'].value())
    script_last_frame = int(nuke.root()['last_frame'].value())

    for i in retime_nodes:
        top_read = find_upstream_reads(retime_nodes)# slice to get the Read´s name
        read_first_frame = int(top_read["first"].getValue())
        read_last_frame = int(top_read["last"].getValue())
        retime_output_first = i["output.first"].getValue()
        retime_output_last = i["output.last"].getValue()
        offset = script_last_frame - retime_output_first
        in_point = read_first_frame + offset
        out_point = 0

        write_jason()


def get_json():
    """
    :return:
    """
    json_dir = "{}".format(PATH)

    if not os.path.exists(json_dir):
        os.makedirs(json_dir)

    jason_path = "{}/log.json".format(json_dir)

    if not os.path.exists(jason_path):
        data = {}
    else:
        _file = open(jason_path, "r")
        data = jason.load(file)

    return data,jason_path


def write_jason(offset):
    """

    :return:
    """
    script_path = nuke.root()['name'].value()
    regex = re.search(r"projects/(\w+)/shots/(\w+)",script_path) #tweak this expression to corresponding fbb path style

    if regex:
        shot = "%s_%s" % (regex.group(1), regex.group(2))
    else:
        print "Invalid Path"
        return

    jason = get_json()
    data = jason[0]
    jason_path = jason[1]

    if data.has_key(shot):
        data[shot] += TIMER
    else:
        data[shot] = TIMER

    _file = open(json_path, "w")
    json.dump(data, _file)
    print data

#CLASSES

class get_retime():

    def get_jason(self):
        self.nodes = nuke.allNodes("Retime")


#CALLS

get_json()
