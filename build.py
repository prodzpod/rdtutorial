import json
from cgi import escape
print("Build started.")

with open("template.html", "r") as f:
    template = f.read()
print("Template loaded.")

with open("./category/Main.json", "r") as f:
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
        with open("./content/" + page_name + ".json", "r") as f:
            meta = json.load(f)
        print(page_name + " page loaded. (" + str(j + 1) + "/" + str(len(pages)) + ").")
        # actually begin loading pages
        page = template.replace("[[TITLE]]", page_name)
        page = page    .replace("[[TAGS]]", ', '.join(meta["tags"]))
        # construct navbar
        navbar = ""
        for k in categories:
            navbar += '<div class="navbar-element hlist"><a href="./' + k\
                   + '.html" class="center vlist" style="width: ' + str(100 / len(main["categories"]) - 2) + 'vw;"><p class="middle">' + k +'</p></a></div>'
        page = page    .replace("[[NAVBAR]]", navbar)
        # construct sidebar
        sidebar = ""
        # TODO: elipses sidebar
        for k in pages:
            sidebar += '<div class="sidebar-element">' + ('&nbsp;' * (2 * k[1]))\
                    + '<a href="./' + k[0] + '.html">' + k[0] + '</button></div>'
        page = page    .replace("[[SIDEBAR]]", sidebar)
        # TODO: previous/next entry thing
        with open("./docs/" + escape(page_name).replace(" ", "%20") + ".html", "w") as f:
            f.write(page)
        print(page_name + " written.")