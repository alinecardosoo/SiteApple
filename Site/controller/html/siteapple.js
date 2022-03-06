function confirmar_deletar_produto(id_produto){

let del= confirm("Deseja realmente excluir este produto?");


if(del==true){ 

window.location.href="delete?id_produto="+id_produto

} else{

window.location.href="product"

}

}