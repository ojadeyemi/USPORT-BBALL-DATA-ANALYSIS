# Draw an NBA court
from sportypy.surfaces.basketball import NBACourt
import matplotlib.pyplot as plt

nba = NBACourt( ).draw()
plt.savefig('BallCourt2', dpi=300)

