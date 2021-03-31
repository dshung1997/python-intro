/**
 * @param {string} s
 * @return {string}
 */
var decodeString = function(s) {
  const generate = ({freq, text}) => {
    return text.repeat(freq);
  };

  let decodedString = "";
  const stack = [];

  let tempNumber = "";
  let tempNode = null;
  
  [...s].forEach((c, i) => {
      if ("0" <= c && c <= "9") {
        tempNumber += c;
      } else if ("a" <= c && c <= "z") {
        if (stack.length === 0) {
          decodedString += c;
        } else if (tempNode) {
          if (tempNode.text) {
            tempNode.text += c;
          } else {
            tempNode.text = c;
          }
        } else {
          const node = stack[stack.length - 1];
          
          if (node.text) {
            node.text += c;
          } else {
            node.text = c;
          }
        }

      } else if (c === "[") {
        const n = parseInt(tempNumber);
        tempNumber = "";
        
        tempNode = {freq: n, text: ""};
        stack.push(tempNode);

      } else if (c === "]") {
        tempNode = null;
        const text = generate(stack.pop());

        if (stack.length === 0) {
          decodedString += text;
        } else {
          const node = stack[stack.length - 1];
          node.text += text;
        }
      }
  });

  return decodedString;
};

// console.log(decodeString("3[z]2[2[y]pq4[2[jk]e1[f]]]ef"));

