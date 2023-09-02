(function(win,doc){
    "use strict";

//Verifica se o usuário quer excluir o dado    
     if(doc.querySelector('.btnDel')){
        let btnDel = doc.querySelectorALL('.btnDel');
        for(let i=0; i< btnDel.lenght; i++){
            btnDel[i].addEventeListener('click',function(event){
                if(confirm('Deseja mesmo apagar este dado?')){
                    return true;
                }else{
                    event.preventDefault();
                } 
            });       
        }        
    }       
})(window,document);    