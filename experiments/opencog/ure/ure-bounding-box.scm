(use-modules (opencog logger))

(load-from-path "conjunction-rule-base-config.scm")

(Concept "BB1")
(Concept "BB2")
(Concept "BoundingBox")

(Inheritance (stv 0.99 0.99) (Concept "BB1") (Concept "BoundingBox"))
; default truth value 1.0 0.0 give 1.0 0 for any inference 
(Inheritance (stv 0.99 0.99) (Concept "BB2") (Concept "BoundingBox"))

(define Herring (Predicate "Herring"))
(define Red (Predicate "Red"))


(define (redness box ) 
    (display "redness called with: ")
    (display box)
    (display "\n")
    (stv 0.55 (random 1.0)) 
)

(define RedBox1
    (EvaluationLink
         (GroundedPredicateNode  "scm: redness")
         (ListLink (
                    TypedVariableLink (Variable "$X"))
                    )
    )
)

(define RedBox2
   (EvaluationLink (stv 0.56 0.7)
         Red
         (ListLink(
             ConceptNode "BB2"
              ))
   )
)

(define HerringBox1 (Evaluation (stv 0.9 0.8) Herring (ConceptNode "BB1")))
(define HerringBox2 (Evaluation (stv 0.9 0.8) Herring (ConceptNode "BB2")))

; need to restrict the search by inheritance link
(define HerringAndRedBox1 (AndLink RedBox1 HerringBox1 (InheritanceLink (VariableNode "$X") (ConceptNode "BoundingBox")) ) )
; don't need to restrict the search by inheritance link here
; do it anyway
(define HerringAndRedBox2 (AndLink RedBox2 HerringBox2  (InheritanceLink (ConceptNode "BB2") (ConceptNode "BoundingBox"))  ))
   

(define (run-bc and-box) 
    (define result (conj-bc and-box))
    (display "\n")
    (display result)
    (display "truth value for the first element in the set\n")
    (display (cog-tv (car (cog-outgoing-set result))))
    (display "\n")
    result
)

(ure-logger-set-level! "trace")
(cog-logger-set-level! "trace")
(ure-set-num-parameter conjunction-rule-base "URE:maximum-iterations" 20)
(run-bc HerringAndRedBox1)
;(run-bc HerringAndRedBox2)
