from interncsfsu import db
from interncsfsu.objects.models import Internship
def keyword_search(keyword):
    query = '\%%s\%' % (keyword)
    results = Internship.query.filter_by(Internship.description.like(query)).all()
    return results
