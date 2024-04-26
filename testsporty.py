# Draw an NBA court
#just tseting out sportpy package
from sportypy.surfaces.basketball import NBACourt
import matplotlib.pyplot as plt

nba = NBACourt(color_updates={
            "plot_background": "#000000",
            "defensive_half_court": "#ffffff",
            "offensive_half_court": "#008fff",
            "court_apron": "#098888",
            "center_circle_outline": "#000000",
            "center_circle_fill": "#ffffff"}).draw()
#plt.savefig('BallCourt2', dpi=300)
plt.show()

