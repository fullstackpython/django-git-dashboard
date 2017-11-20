import os
from git import Repo


repo_path = os.getenv('GIT_REPO_PATH')

repo = Repo(repo_path)

if not repo.bare:
    print('Repo at {} successfully loaded.'.format(repo_path))

last_commit = repo.head.commit

print("\"{}\" by {}".format(last_commit.summary, last_commit.author.name))
print(str(last_commit.size))
