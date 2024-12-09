#include <pybind11/pybind11.h>
#include <pybind11/stl.h>
#include "brain_region_analysis.hpp"

class PyTreeNode {
public:
    int intensity;
    std::shared_ptr<PyTreeNode> left;
    std::shared_ptr<PyTreeNode> right;

    PyTreeNode(int val) : intensity(val), left(nullptr), right(nullptr) {}
};

int py_analyzeBrainRegions(std::shared_ptr<PyTreeNode> root, int low, int high) {
    std::function<std::shared_ptr<TreeNode<int>>(std::shared_ptr<PyTreeNode>)> convert = [&convert](std::shared_ptr<PyTreeNode> node) -> std::shared_ptr<TreeNode<int>> {
        if (!node) {
            return nullptr;
        }
        auto cpp_node = std::make_shared<TreeNode<int>>(node->intensity);
        cpp_node->left = convert(node->left);
        cpp_node->right = convert(node->right);
        return cpp_node;
    };

    std::shared_ptr<TreeNode<int>> cpp_root = convert(root);
    return analyzeBrainRegions(cpp_root.get(), low, high);
}

PYBIND11_MODULE(brain_region_analysis, m) {
    m.doc() = "Brain region analysis module for medical imaging";

    pybind11::class_<PyTreeNode, std::shared_ptr<PyTreeNode>>(m, "TreeNode")
        .def(pybind11::init<int>())
        .def_readwrite("intensity", &PyTreeNode::intensity)
        .def_readwrite("left", &PyTreeNode::left)
        .def_readwrite("right", &PyTreeNode::right);

    m.def("analyze_brain_regions", &py_analyzeBrainRegions,
          "Analyze brain regions and sum intensities within a given range",
          pybind11::arg("root"), pybind11::arg("low"), pybind11::arg("high"));
}
