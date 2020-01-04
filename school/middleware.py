from project.models import Project


class SchoolMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        project_code = request.session.get('project_code', None)
        if project_code:
            request.PROJECT = Project.pull(project_code)
        else:
            request.PROJECT = Project.pull()
        request.session['project_code'] = request.PROJECT.code

        response = self.get_response(request)
        return response
