import os
from git import Repo
#from analyzer.models import GitRepository, GitCommit


def print_commit(commit):
    print('----')
    print(str(commit.hexsha))
    print("\"{}\" by {} ({})".format(commit.summary,
                                     commit.author.name,
                                     commit.author.email))
    print(str(commit.authored_datetime))
    print(str("count: {} and size: {}".format(commit.count(),
                                              commit.size)))
    print(str(commit.size))


def create_repository(repo):
    repo = GitRepository()

    repo.save()
    return repo


def create_commit(commit):
    gc = GitCommit()
    gc.checksum_hash = commit.hexsha
    gc.count = commit.count()
    gc.author_name = commit.author.name
    gc.author_email = commit.author.email
    gc.commit_date = commit.authored_datetime
    # TODO: check for parents and add them
    gc.save()
    return gc


if __name__ == "__main__":
#def load():
    repo_path = os.getenv('GIT_REPO_PATH')

    repo = Repo(repo_path)


    if not repo.bare:
        print('Repo at {} successfully loaded.'.format(repo_path))

    # check out last commit
    last_commit = repo.head.commit
    print_commit(last_commit)

    # go through all commits
    commits = list(repo.iter_commits('master'))
    for commit in commits:
        print_commit(commit)

