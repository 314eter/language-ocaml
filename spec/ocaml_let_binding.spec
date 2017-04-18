// SYNTAX TEST "source.ocaml"
let x a = 1 in 2
//<- keyword.other.function-definition.ocaml
//  ^ entity.name.function.ocaml
//      ^ punctuation.separator.assignment.ocaml
//          ^^ keyword.other.in.ocaml
//^^^^^^^^^^^^ meta.let_binding.ocaml
//            ^^ !meta.let_binding.ocaml

let x = 1 and y = 2 in 3
//<- keyword.other.function-definition.ocaml
//  ^ entity.name.function.ocaml
//    ^ punctuation.separator.assignment.ocaml
//        ^^^ keyword.other.function-definition.ocaml
//            ^ entity.name.function.ocaml
//              ^ punctuation.separator.assignment.ocaml
//                  ^^ keyword.other.in.ocaml
//^^^^^^^^^^^^^^^^^^^^ meta.let_binding.ocaml
//                    ^^ !meta.let_binding.ocaml

let x = 1 and y = 2 and z = 3 in 4
//<- keyword.other.function-definition.ocaml
//  ^ entity.name.function.ocaml
//    ^ punctuation.separator.assignment.ocaml
//        ^^^ keyword.other.function-definition.ocaml
//            ^ entity.name.function.ocaml
//              ^ punctuation.separator.assignment.ocaml
//                  ^^^ keyword.other.function-definition.ocaml
//                      ^ entity.name.function.ocaml
//                        ^ punctuation.separator.assignment.ocaml
//                            ^^ keyword.other.in.ocaml
//^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ meta.let_binding.ocaml
//                              ^^ !meta.let_binding.ocaml

let x = 1
//<- keyword.other.function-definition.ocaml
//  ^ entity.name.function.ocaml
//    ^ punctuation.separator.assignment.ocaml
//^^^^^^^ meta.let_binding.ocaml
and y = 2
//<- keyword.other.function-definition.ocaml
//  ^ entity.name.function.ocaml
//^^^^^^^ meta.let_binding.ocaml
in 3
//<- keyword.other.in.ocaml
//<- meta.let_binding.ocaml
//^^ !meta.let_binding.ocaml
