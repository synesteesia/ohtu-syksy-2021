from matchers import And, HasFewerThan, Or, HasAtLeast, PlaysIn, Not, All

class QueryBuilder:
  def __init__(self):
    self._matchers = [All()]

  def build(self):
    matchers = self._matchers
    self._matchers = []
    return And(*matchers)

  def playsIn(self, team):
    self._matchers.append(PlaysIn(team))
    return self

  def hasAtLeast(self, value, attr):
    self._matchers.append(HasAtLeast(value, attr))
    return self

  def hasFewerThan(self, value, attr):
    self._matchers.append(HasFewerThan(value, attr))
    return self

  def oneOf(self,*matchers):
    self._matchers = [Or(*matchers)]
    return self