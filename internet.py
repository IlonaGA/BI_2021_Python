# %% Internet hw

import requests
from bs4 import BeautifulSoup as bs

# %%


def save_content(req, filename):
    with open(filename, 'wb') as file:
        file.write(req.content)


# %%


def get_user_info(user_name):
    req = requests.get(f'https://github.com/{user_name}/')
    soup = bs(req.content)
    try:
        class_name = 'p-name vcard-fullname d-block overflow-hidden'
        name = soup.find(class_=class_name).getText().strip()
    except:
        name = ''

    try:
        organisation = soup.find(class_='p-org').getText()
    except:
        organisation = ''

    try:
        location = soup.find(class_='p-label').getText()
    except:
        location = ''

    # Not really good solution, but simple
    try:
        followers = soup.find(class_='text-bold color-fg-default').getText()
    except:
        followers = ''

    try:
        repositories = soup.find(class_='Counter').getText()
    except:
        repositories = ''

    # save_content(req, 'test.txt')

    return {'name': name,
            'organisation': organisation,
            'location': location,
            'followers': followers,
            'repositories': repositories}

# %%


def get_user_repositories(username):
    req = requests.get(f'https://github.com/{username}?tab=repositories')
    soup = bs(req.content)

    class_name = 'col-12 d-flex width-full'
    class_name += ' py-4 border-bottom color-border-muted public source'
    repositories = soup.find_all(class_=class_name)
    ans = []
    for counter, rep in enumerate(repositories):
        item = {}
        item['user'] = username
        try:
            item['repository'] = rep\
                .find(itemprop='name codeRepository')\
                .getText().strip()
        except:
            item['repository'] = 'None'

        try:
            item['language'] = rep\
                .find(itemprop='programmingLanguage')\
                .getText()
        except:
            item['language'] = 'None'
        ans.append(item.copy())

    print(counter)
    return ans

# %%


def download_file(username, repository, remote_file_path, local_file_path):
    link = f'https://raw.githubusercontent.com'
    link += '/{username}/{repository}/master/{remote_file_path}'
    req = requests.get(link)

    save_content(req, local_file_path)

if __name__ == '__main__':

    print('example get_user', get_user_info('IlonaGA'))
    print('example get repositories', get_user_repositories('IlonaGA'))
    print('example dowload file',
          download_file('IlonaGA', 'MyFirstDash',
                        'dashapp.py', 'my_dashapp.py'))
