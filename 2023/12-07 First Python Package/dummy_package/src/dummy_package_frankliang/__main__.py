

class Nobles:
    class_name=None
    title=None
    def __init__(self) -> None:
        pass
    def scream(self):
        print('Oh my god')
    def address(self):
        print('you address {class_name} the {title}'.format(**{
            "class_name":self.class_name,
            "title":self.title
        }))


class King(Nobles):
    class_name='the King'
    title = 'Your Majasty'
    __in_thron__ = 0
    def __init__(self) -> None:
        
        if King.__in_thron__ >= 1:
            raise Exception('There may only be one king')
        else:
            King.__in_thron__ += 1      

    def scream(self):
        print('Oh Queen mother!')


class Duke(Nobles):
    class_name='the Duke'
    title = ''
    def __init__(self, name='nameless duke') -> None:
        self.name = name
    def scream(self):
        print('Oh no!')