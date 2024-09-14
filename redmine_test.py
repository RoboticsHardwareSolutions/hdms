from redminelib import Redmine

if __name__ == "__main__":

    redmine = Redmine(, key='')
    project = redmine.project.get('')
    print(project.id)
    print(project.name)
    project = redmine.project.get('')
    print(project.id)
    print(project.name)

    projects = redmine.project.all()
    for project in projects:
        print(str(project.id) + " - " + project.name)

    issues = redmine.issue.filter(project_id=6, tracker_id=7)
    for issue in issues:
        print(issue.subject)

    tracker = redmine.tracker.all()
    for track in tracker:
        print(str(track.id) + ' ' + track.name + ' ' + track.description)

    issue = redmine.issue.get(1234)
    print(issue.subject + " - " + str(issue.status))
