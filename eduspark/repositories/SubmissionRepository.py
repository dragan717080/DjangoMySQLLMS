from ..models import Submission
from .AssignmentRepository import AssignmentRepository
from .BaseRepository import BaseRepository

class SubmissionRepository(BaseRepository):
    def __init__(self):
       self.model = Submission
       self.assignment_repository = AssignmentRepository()

    def create(self, title, content, assignment_id, order):
        assignment = self.assignment_repository.get_by_id(assignment_id)
        if not assignment:
            return "Assignment does not exist"
        submission = Submission(title=title, content=content, assignment_id=assignment.id, order=order)
        submission.save()
        return submission

    def update(self, id, title, content, assignment_id, order):
        try:
          submission = Submission.objects.get(pk=id)
        except Submission.DoesNotExist:
            return None

        if title:
            submission.title = title

        if content:
          submission.content = content

        if order:
            submission.order = order

        assignment = self.assignment_repository.get_by_id(assignment_id)
        if not assignment:
            return "assignment does not exist"

        submission.save()
        return submission
