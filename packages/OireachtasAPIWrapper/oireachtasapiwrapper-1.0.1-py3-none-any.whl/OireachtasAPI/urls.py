

class URLs:

    def __init__(self):
        self.base_url = 'https://api.oireachtas.ie/v1'

        #endpoints
        self.legislation = "/legislation"
        self.debates = '/debates'
        self.constituencies = '/constituencies'
        self.parties = '/parties'
        self.divisions = '/divisions'
        self.questions = '/questions'
        self.houses = '/houses'
        self.members = '/members'

    """Merges all the base urls with their respecitve endpoints and returns them
    All of these are hidden methods as to not pollute the namespace"""
    def _base_url(self):
        return self.base_url

    def _legislation_url(self):
        return self.base_url + self.legislation

    def _debates_url(self):
        return self.base_url + self.debates

    def _constituencies_url(self):
        return self.base_url + self.constituencies

    def _parties_url(self):
        return self.base_url + self.parties

    def _divisions_url(self):
        return self.base_url + self.divisions

    def _questions_url(self):
        return self.base_url + self.questions

    def _houses_url(self):
        return self.base_url + self.houses

    def _members_url(self):
        return self.base_url + self.members
