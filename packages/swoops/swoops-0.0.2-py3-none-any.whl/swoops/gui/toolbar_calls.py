"""
Written by Jason Krist
06/20/2024

"""

from .. import constants as CONS


def project_trace(integrator):
    """project trace as 2 item list"""
    project = integrator.session.projects[integrator.active_ids["project"]]
    pid = getattr(project, CONS.ID)
    return [str(pid), "projects"]


def workflow_trace(integrator):
    """workflow trace as 4 item list"""
    project = integrator.session.projects[integrator.active_ids["project"]]
    pid = getattr(project, CONS.ID)
    workflow = project.workflows[integrator.active_ids["workflow"]]
    wid = getattr(workflow, CONS.ID)
    return [str(wid), "workflows", str(pid), "projects"]


def study_trace(integrator):
    """study trace as 4 item list"""
    project = integrator.session.projects[integrator.active_ids["project"]]
    pid = getattr(project, CONS.ID)
    if integrator.active_ids["study"] > 0:
        study = project.studies[integrator.active_ids["study"]]
        sid = getattr(study, CONS.ID)
        return [str(sid), "studies", str(pid), "projects"]


def analysis_trace(integrator):
    """study trace as 4 item list"""
    project = integrator.session.projects[integrator.active_ids["project"]]
    pid = getattr(project, CONS.ID)
    if integrator.active_ids["analysis"] > 0:
        analysis = project.analyses[integrator.active_ids["analysis"]]
        aid = getattr(analysis, CONS.ID)
        return [str(aid), "analyses", str(pid), "projects"]


def new_project(integrator):
    """new project"""
    trace = ["projects"]
    integrator.exec(trace, {"old": None, "new": None})

def open_project(integrator):
    print("open project")


def save_project(integrator):
    print("save project")

def save_as_project(integrator):
    print("save project")

def new_workflow(integrator):
    """new workflow"""
    trace = ["workflows"] + project_trace(integrator)
    integrator.exec(trace, {"old": None, "new": None})


def new_task(integrator):
    """new task"""
    trace = ["tasks"] + workflow_trace(integrator)
    integrator.exec(trace, {"old": None, "new": None})


def new_group(integrator):
    """new_group"""
    trace = ["groups"] + workflow_trace(integrator)
    integrator.exec(trace, {"old": None, "new": None})


def new_pool(integrator):
    """new pool"""
    trace = ["pools"] + workflow_trace(integrator)
    integrator.exec(trace, {"old": None, "new": None})


def new_input(integrator):
    """new input"""
    trace = ["inputs"] + workflow_trace(integrator)
    integrator.exec(trace, {"old": None, "new": None})


def new_output(integrator):
    """new output"""
    trace = ["outputs"] + workflow_trace(integrator)
    integrator.exec(trace, {"old": None, "new": None})


def new_run_creator(integrator):
    """new doe"""
    trace = ["run_creators"] + study_trace(integrator)
    integrator.exec(trace, {"old": None, "new": None})


def new_constraint(integrator):
    """new constraint"""
    trace = ["constraints"] + study_trace(integrator)
    integrator.exec(trace, {"old": None, "new": None})


def new_objective(integrator):
    """new objective"""
    trace = ["objectives"] + study_trace(integrator)
    integrator.exec(trace, {"old": None, "new": None})


def new_toolbar_button(_integrator):
    """create a custom toolbar button"""
    print("new toolbar button")


def ph(_integrator):
    """placeholder callback"""
    print("placeholder callback")
