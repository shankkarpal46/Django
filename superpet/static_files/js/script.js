function updateQuantity(operation,productId)
{
   const inputBox= document.getElementById("quantity"+productId);
   inputBox.value=parseInt(inputBox.value)+operation;


   // value=parseInt(inputBox.value)
   // if (value >=0 && value <= 10){
   //     inputBox.value=parseInt(inputBox.value)+operation;
   // }
   // if (inputBox.value >=0){
   //    inputBox.value=parseInt(inputBox.value)+operation;
   // }

   // if(inputBox.value <= 10){
   //    inputBox.value=parseInt(inputBox.value)+operation;
   // }
}