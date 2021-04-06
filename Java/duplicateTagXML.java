import java.io.*;
import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;
import org.w3c.dom.Document;
import org.w3c.dom.*;
import java.util.Arrays;

import javax.xml.transform.*;
import javax.xml.transform.dom.*;
import javax.xml.transform.stream.*;


import javax.xml.parsers.DocumentBuilderFactory;
import javax.xml.parsers.DocumentBuilder;
import org.xml.sax.SAXException;
import org.xml.sax.SAXParseException;


public class TakeDuplicatesXml{

    public static void main(String[] args){

        try{
            DocumentBuilderFactory docFactory = DocumentBuilderFactory.newInstance();
            DocumentBuilder docBuilder = docFactory.newDocumentBuilder();
            Document doc = docBuilder.parse("/Users/youruser/code/Exercises/file.xml");

            //get node list
            List<String> aux = new ArrayList<String>();
            removeDuplicate(doc.getDocumentElement(), aux);

            //print the new document out
            printXmlDocument(doc);
        } catch (Exception ex) {
            ex.printStackTrace();
        }
    }

    public static void printXmlDocument(Document doc){
        try{
            DOMSource domSource = new DOMSource(doc);
            StringWriter writer = new StringWriter();
            StreamResult result = new StreamResult(writer);
            TransformerFactory tf = TransformerFactory.newInstance();
            Transformer transformer = tf.newTransformer();
            transformer.transform(domSource, result);
            System.out.println("XML IN String format is: \n" + writer.toString());
        }catch (Exception ex) {
            ex.printStackTrace();
        }

    }
  //with recursion
    public static void removeDuplicate(Node node, List<String>  aux){

        System.out.println(node.getNodeName());
        //check if that node exists already
        if(aux.contains(node.getNodeName())){
            node.getParentNode().removeChild(node);
        }else{
            //add node name to aux list
            aux.add(node.getNodeName());
        }

        NodeList nodeList = node.getChildNodes();

        for (int i = 0; i < nodeList.getLength(); i++) {
            Node currentNode = nodeList.item(i);
            if (currentNode.getNodeType() == Node.ELEMENT_NODE) {
                //calls this method for all the children which is Element
                removeDuplicate(currentNode, aux);
            }
        }
    }
}