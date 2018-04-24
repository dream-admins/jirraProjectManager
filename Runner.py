import requests
from pynput import keyboard
from JItem import JItem
from JTable import JTable
from requests.auth import HTTPBasicAuth
import datetime

__table = JTable()

def main():

    baseAuth = HTTPBasicAuth('taras', 'werthrb')
    response = authToJira('https://charmtech.atlassian.net/rest/api/2/search?jql=filter=14202', baseAuth)
    items = getItemList(response.json())
    __table.setItems(items)

    with keyboard.Listener(
            on_press=on_press) as listener:
        listener.join()
    # Collect events until released
 #   input()

def authToJira(url, baseAuth):
    resp = requests.get(url, auth=baseAuth)
    return resp

def getItemList(json):
    items = []
    index = 0
    it = iter(json['issues'])
    for issue in it:
        row = JItem()
        row.setOrder(index)
        row.setKey(issue['key'])
        row.setSummaryText(issue['fields']['summary'].encode('ascii', 'ignore').decode('ascii'))
        row.setSelected(False)
        items.append(row)
        index += 1
    return items

def on_press(key):
    try:
        if key == keyboard.Key.up:
            __table.moveUp()
        if key == keyboard.Key.down:
            __table.moveDown()

        if key == keyboard.Key.insert:
            __table.selectCurrent()


        if key == keyboard.Key.esc:
            return False

    except AttributeError:
        print('special key {0} pressed'.format(
            key))


if __name__ == '__main__':
    main()