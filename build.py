import os
import re
import json
def touch(fname, times=None):
    with open(fname, 'a'):
        os.utime(fname, times)

print("Build started.")
MAIN_JSON = "Getting Into It"
###############################################################################
with open("replacekey.json", "r") as f:
    replaces = json.load(f)
print("Replace keys loaded.")

for root, dirs, files in os.walk("./content"):
    for file in files:
        with open(os.path.join(root, file), "r") as f:
            doc = f.read()
        for repl in replaces["simple"].items():
            doc = doc.replace(repl[0], repl[1])
        for repl in replaces["regex"].items():
            doc = re.sub(repl[0], repl[1], doc)
        for matches in re.findall("\\*\\*.+?\\*\\*", doc):
            txt = "<span class=\"b\" id=\"" + matches[2:-2] + "\">"
            for letter in enumerate(matches[2:-2]):
                l = letter[1]
                if (l == ' '):
                    l = '&nbsp;'
                txt += "<b style=\"--d:" + str(letter[0]) + "\">" + l + "</b>"
            txt += "</span>"
            doc = doc.replace(matches, txt)
        with open(os.path.join("./docs/public/pages/", file), "w+") as f:
            f.write(doc)
###############################################################################
with open("template.html", "r") as f:
    template = f.read()
print("Template loaded.")

with open("./category/" + MAIN_JSON + ".json", "r") as f:
    main = json.load(f)
print("Main JSON loaded.")
categories = main["categories"]
print("Detected " + str(len(categories)) + " categories.")
# only Main has duplicate pages, so load everything else, then the main page

for i in range(len(categories)):
    with open("./category/" + categories[i] + ".json", "r") as f:
        category = json.load(f)
    print(categories[i] + " JSON loaded (" + str(i + 1) + "/" + str(len(categories)) + ").")
    pages = category["pages"]
    print(str(len(pages)) + " page(s) detected.")

    for j in range(len(pages)): # [name, indent]
        page_name = pages[j][0]
        if not os.path.exists("./content/" + page_name + ".md"):
            touch("./content/" + page_name + ".md")
            touch("./docs/public/pages/" + page_name + ".md")
        print(page_name + " page loaded. (" + str(j + 1) + "/" + str(len(pages)) + ").")
        # actually begin loading pages
        page = template.replace("[[TITLE]]", page_name)
        # construct navbar
        navbar = ""
        for k in categories:
            navbar += '<div class="navbar-element hlist"><a href="./' + k\
                    + '.html" class="center" style="width: ' + str(100 / len(main["categories"]) - 2) + 'vw;"><p class="middle"><black>' + k +'</black></p></a></div>'
        page = page    .replace("[[NAVBAR]]", navbar)
        # construct sidebar
        sidebar = ""
        for k in pages:
            sidebar += '<div class="sidebar-element">' + ('&nbsp;' * (2 * k[1]))\
                    + '<a href="./' + k[0] + '.html">' + k[0] + '</a></div>'
        page = page    .replace("[[SIDEBAR]]", sidebar)
        # construct endmenu
        endmenu = ""
        k = 0
        endmenu += '<div id="endmenu" class="endmenu hlist" style="width:' + str(round(len(pages) / 4 + 0.25) * 100) +'vw">'
        while 1:
            if (k >= len(pages)):
                break
            endmenu += '<div class="endmenu-row vlist">'
            for m in range(4):
                if (k < len(pages)):
                    endmenu += '<div class="endmenu-element">' + ('&nbsp;' * (2 * pages[k][1]))\
                            + '<a href="./' + pages[k][0] + '.html"><black>' + pages[k][0] + '</black></a></div>'
                else:
                    endmenu += '<div class="endmenu-blank"></div>'
                k += 1
            endmenu += '</div>'
        endmenu += '</div>'
        page = page.replace("[[ENDMENU]]", endmenu)
        # prev/next on lists...
        if j == 0:
            page = page.replace("[[URLLEFT]]", '#')
            page = page.replace("[[TITLELEFT]]", 'This is the first article.')
        else:
            page
            page = page.replace("[[URLLEFT]]", './' + pages[j-1][0] + '.html')
            page = page.replace("[[TITLELEFT]]", pages[j-1][0])
        if j == len(pages) - 1:
            page = page.replace("[[URLRIGHT]]", '#')
            page = page.replace("[[TITLERIGHT]]", 'This is the last article.')
        else:
            page = page.replace("[[URLRIGHT]]", './' + pages[j+1][0] + '.html')
            page = page.replace("[[TITLERIGHT]]", pages[j+1][0])
        with open("./docs/" + page_name + ".html", "w") as f:
            f.write(page)
        print(page_name + " written.")