#include <pybind11/pybind11.h>
#include <pybind11/stl.h>
#include "terrain_navigation_dem_tracker.hpp"

PYBIND11_MODULE(terrain_navigation_tracker, m) {
    m.doc() = "UAS Terrain-Referenced Navigation System";

    pybind11::class_<TreeNode>(m, "TreeNode")
        .def(pybind11::init<int>())
        .def_readwrite("elevation", &TreeNode::elevation)
        .def_readwrite("left", &TreeNode::left)
        .def_readwrite("right", &TreeNode::right);

    m.def("sum_elevation_range", &UASTerrainNavigation::sumElevationRange,
        "Calculate the sum of elevations within the given range");
    m.def("build_dem_tree", &UASTerrainNavigation::buildDEMTree,
        "Build a Digital Elevation Model tree from a list of elevations");
}
