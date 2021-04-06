public class TakeDuplicatesXml{

    public static void main(String[] args) throws IOException{

        DocumentBuilderFactory docFactory = DocumentBuilderFactory.newInstance();
        DocumentBuilder docBuilder = docFactory.newDocumentBuilder();
        Document doc = docBuilder.parse("/Users/youruser/code/Exercises/file.xml");

        List<String> duplicateTagList = new ArrayList<String>();
        removeDuplicate(doc.getDocumentElement(), duplicateTagList);

        //print the new document out
        printXmlDocument(doc);
    }
    public static void removeDuplicate(Node node, List<String>  duplicateTagList) throws IOException{

        System.out.println(node.getNodeName());

        if(duplicateTagList.contains(node.getNodeName())){
            node.getParentNode().removeChild(node);
        }else{
            duplicateTagList.add(node.getNodeName());
        }

        NodeList nodeList = node.getChildNodes();
        for (int i = 0; i < nodeList.getLength(); i++) {
            Node currentNode = nodeList.item(i);
            if (currentNode.getNodeType() == Node.ELEMENT_NODE) {
                removeDuplicate(currentNode, duplicateTagList);
            }
        }
    }
}