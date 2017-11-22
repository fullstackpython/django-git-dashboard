import os
from git import Repo


def parse_commit(commit):
    print("\"{}\" by {}".format(commit.summary, commit.author.name))
    print(str(commit.authored_datetime))
    print(str(commit.size))


if __name__ == "__main__":
    repo_path = os.getenv('GIT_REPO_PATH')

    repo = Repo(repo_path)

    if not repo.bare:
        print('Repo at {} successfully loaded.'.format(repo_path))

    # check out last commit
    last_commit = repo.head.commit
    parse_commit(last_commit)

    # go through all commits
    commits = list(repo.iter_commits('master'))
    for commit in commits:
        parse_commit(commit)

