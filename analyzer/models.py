from django.db import models


class GitRepository(models.Model):
    """Represents a single Git repository and its metadata. Each commit is
    stored in its own repository.
    """
    git_url = models.CharField(max_length=1024, blank=True)
    local_location = models.CharField(max_length=1024, blank=True)


class GitCommit(models.Model):
    """A single Git commit and its metadata."""
    repository = models.ForeignKey('GitRepository')
    checksum_hash = models.CharField(max_length=40)
    count = models.IntegerField()
    summary = models.TextField(blank=True)
    author_name = models.CharField(max_length=256)
    author_email = models.CharField(max_length=256)
    commit_date = models.DateTimeField()
    parents = models.ManyToManyField('GitCommit')

    def __unicode__(self):
        return checksum_hash

