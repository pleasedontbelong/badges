from extended_choices import Choices
from datetime import timedelta

BADGES = Choices(
    ("STAR", 1, "Star"),
    ("COLLECTOR", 2, "Collector"),
    ("PIONNEER", 3, "Pionneer"),
)

NB_VIEWS_FOR_STAR = 1000
NB_MODELS_FOR_COLLECTOR = 5
TIMEDELTA_FOR_PIONNEER = timedelta(days=365)
