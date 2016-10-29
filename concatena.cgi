#!/usr/bin/perl
use CGI;
$cgi = new CGI;

print $cgi->header(-charset => 'utf-8');
print $cgi->start_html('CGI conacatena strings');

if(!$cgi->param){
 print $cgi->start_form;
 print $cgi->p('Nombre');
 print $cgi->textfield(-name=>'nombre',-size=>30);
 print $cgi->p('Apellido');
 print $cgi->textfield(-name=>'apellido',-size=>20);
 print $cgi->submit(-value=>'enviar');
 print $cgi->end_form;
}else{
 # if empty fields? 
 #
 $cadena= $cgi->param('nombre');
 $cadena2= $cgi->param('apellido');
 print $cgi->h3('mi nombre es ' . $cadena . ' y mi apellido es ' . $cadena2);
}
print $cgi->end_html;
