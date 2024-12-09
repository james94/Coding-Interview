#include <pybind11/pybind11.h>
#include <pybind11/stl.h>
#include "sdc_safety_score_tracker.hpp"

PYBIND11_MODULE(sdc_safety_score_tracker, m) {
    pybind11::class_<DecisionNode, std::shared_ptr<DecisionNode>>(m, "DecisionNode")
        .def(pybind11::init<int>())
        .def_readwrite("safety_score", &DecisionNode::safety_score)
        .def_readwrite("left", &DecisionNode::left)
        .def_readwrite("right", &DecisionNode::right);

    pybind11::class_<SelfDrivingCarSafetyScoreTracker>(m, "SelfDrivingCarSafetyScoreTracker")
        .def(pybind11::init<>())
        .def("calculate_safety_score", &SelfDrivingCarSafetyScoreTracker::calculateSafetyScore);
}
