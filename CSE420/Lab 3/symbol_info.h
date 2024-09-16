#ifndef SYMBOL_INFO_H
#define SYMBOL_INFO_H

#include <string>
#include "TreeNode.h"

class symbol_info {
private:
    std::string sym_name;
    std::string sym_type;
    TreeNode* syntax_tree_node;

public:
    symbol_info(std::string name, std::string type, TreeNode* node = nullptr)
        : sym_name(name), sym_type(type), syntax_tree_node(node) {}

    std::string getname() const {
        return sym_name;
    }

    std::string gettype() const {    
        return sym_type;
    }

    TreeNode* getNode() const {
        return syntax_tree_node;
    }

    void setNode(TreeNode* node) {
        syntax_tree_node = node;
    }
};

#endif  // SYMBOL_INFO_H
