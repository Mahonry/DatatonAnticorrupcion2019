//Script Con el comando utilizado en MongoDB para hacer las proyecciones con las consultas necesarias a la base de datos.

db.S6_Contrataciones.find({cycle:2018, "tender.procurementMethod": "direct"}, {ocid:1, "buyer.name":1, "contracts":1,"awards.suppliers.name":1}).forEach(function(d) {
var total = 0;
if (typeof d.contracts!== 'undefined'){
  for (var g of d.contracts){
     total += g.value.amount
  } d.total = total;
  db.proyeccion.insertOne(d);}
})
