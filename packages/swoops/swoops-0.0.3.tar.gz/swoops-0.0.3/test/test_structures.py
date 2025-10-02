"""
Written by Jason Krist
05/01/2024
"""

from os import path
import sys

testdir = path.dirname(path.realpath(__file__))
appendpath = path.join(testdir, "../../src")
sys.path.insert(0, appendpath)

from openstudy import structures as cl  # type: ignore # pylint: disable=E0611,E0401,C0413
from openstudy import helper as hp  # type: ignore # pylint: disable=E0611,E0401,C0413


if __name__ == "__main__":
    wf0 = cl.Workflow(_id=69, name="lol")
    wf0.new_node(name="node 1", tid=1, pid=2)
    print(wf0.__dict__)
    print("\n\n")
    print(hp.obj_to_dict(wf0))
    print("\n\n")
    ses0 = cl.Session(0)
    proj0 = ses0.new_project(name="ewwww stinky 3")
    wf1 = proj0.new_workflow(name="first one")
    print(hp.obj_to_dict(ses0))
    print("\n\n")
    print(hp.obj_to_dict(proj0))
    print("\n\n")
    proj0.save_as("./project0_before.toml")
    proj1 = ses0.open_project("./project0_before.toml")
    wf2 = proj1.new_workflow(name="second one")
    wf2.new_node(name="node 1", tid=1, pid=2)
    wf2.new_node(name="node 2", tid=1, pid=2)
    print(hp.obj_to_dict(ses0))
    print("\n\n")
    proj1.save_as("./project1_after.toml")

    nodes_df = hp.dict_to_df(wf2.nodes)
    newcolnames = hp.clean_colnames(nodes_df.columns)
    rename_dict = {nodes_df.columns[i]: nc for i, nc in enumerate(newcolnames)}
    print(rename_dict)
    nodes_df_rename = nodes_df.rename(columns=rename_dict)
    print(nodes_df_rename)
    scriptdir = path.dirname(path.realpath(__file__))
    nodes_df_rename.to_csv(path.join(scriptdir, "./wf2_nodes.csv"), index=False)
