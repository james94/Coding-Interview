import terrain_navigation_tracker as tn

dem1 = [100,50,150,30,70,None,180]
root1 = tn.build_dem_tree(dem1)
result1 = tn.sum_elevation_range(root1, 70, 150)
print(f"Sum of elevations between 70m and 150m: {result1}m")

dem2 = [100,50,150,30,70,130,180,10,None,60]
root2 = tn.build_dem_tree(dem2)
result2 = tn.sum_elevation_range(root2, 60, 100)
print(f"Sum of elevations between 60m and 100m: {result2}m")
