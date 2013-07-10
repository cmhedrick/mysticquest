from bottle import route, run, template, request, response
import loadrooms


@route('/')
def index():
    global our_hero
    our_hero = loadrooms.begin()
    title = our_hero.__str__().split('\n')[0]
    story = our_hero.__str__().split('\n')[1]
    return template('templates/begin.tpl', story=story, title=title)

@route('/moving', method="post")
def journey():
    direction = request.forms.get('direction')
    new_hero = loadrooms.destiny(our_hero, direction)
    title = new_hero.__str__().split('\n')[0]
    story = new_hero.__str__().split('\n')[1]
    import pdb; pdb.set_trace()
    return template('templates/begin.tpl', story=story, title=title)

run(host='localhost', port=8080)
