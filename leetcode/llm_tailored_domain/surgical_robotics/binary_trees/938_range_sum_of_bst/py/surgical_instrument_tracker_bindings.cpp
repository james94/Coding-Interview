#include <pybind11/pybind11.h>
#include <pybind11/stl.h>
#include "surgical_instrument_tracker.hpp"

PYBIND11_MODULE(surgical_instrument_tracker, m) {
    pybind11::class_<SurgicalInstrumentTracker>(m, "SurgicalInstrumentTracker")
        .def(pybind11::init<>())
        .def("insert", &SurgicalInstrumentTracker::insert)
        .def("sum_in_range", &SurgicalInstrumentTracker::sumInRange)
        .def("get_all_distances", &SurgicalInstrumentTracker::getAllDistances)
        .def("display_instrument_movements", &SurgicalInstrumentTracker::displayInstrumentMovements);
}
