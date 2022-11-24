namespace Projector.DSA;

public class BinarySearchTree
{
    public TreeNode? Root { get; set; }

    public BinarySearchTree()
    {
        Root = null;
    }

    public void Insert(int value)
    {
        var newNode = new TreeNode(value);
        if (Root is null)
        {
            Root = newNode;
        }
        else
        {
            TreeNode current = Root!;
            TreeNode parent;
            while (true)
            {
                parent = current!;
                if (value < current!.Value)
                {
                    current = current!.Left!;
                    if()
                }
            }
        }
    }
}