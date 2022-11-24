namespace Projector.DSA;

public class TreeNode
{
    public TreeNode? Left { get; set; }
    public TreeNode? Right { get; set; }
    public int Value { get; set; }

    public TreeNode(int value)
    {
        Value = value;
    }
}