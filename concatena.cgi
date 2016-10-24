#!/usr/bin/perl
use CGI;
$cgi = new CGI;


print $cgi->header;
print $cgi->start_html('titulo');

if(!$cgi->param){
print $cgi->start_form;
print $cgi->textfield(-name=>'nombre',-size=>30);
print $cgi->textfield(-name=>'apellido',-size=>20);
print $cgi->submit(-value=>'enviar');


print $cgi->end_form;


}else{
$cadena= $cgi->param('nombre');
$cadena2= $cgi->param('apellido');
print $cgi->h3('mi nombre es' . $cadena . ' mi apellido es' . $cadena2);


}
print $cgi->end_html;
