
name=""
category=""
    $.get("http://localhost:5000/content",
        {
            name:"KFC"
        },
        false,
        function(data){
            console.log(data)
        });
    $.get("http://localhost:5000/restaurants",
        {
        },
        false,
        function(data){
            console.log(data)
            name=data
            console.log(name)
        });

    

    $.get("http://localhost:5000/categorycontent?name=KFC&category=Chicken",
        {
            category:" "
            name: ""
        },
        function(data) {
            window.obj=JSON.parse(data);
            console.log(obj);
            for(i=0;i<Object.keys(obj).length;i++){
                var d=document.createElement("div");
                d.innerHTML=Object.keys(obj)[i];
                $('#main').append(d);
            }
                // body.document.appenChild(d);
        });