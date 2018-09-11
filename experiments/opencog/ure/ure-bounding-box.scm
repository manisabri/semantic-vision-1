
(load-from-path "conjunction-rule-base-config.scm")

(Concept "BB1")
(Concept "BB2")
(Concept "BoundingBox")

(Inheritance (Concept "BB1") (Concept "BoundingBox"))
(Inheritance (Concept "BB2") (Concept "BoundingBox"))

(define Herring (Predicate "Herring"))
(define Red (Predicate "Red"))


(define (redness box color) (cog-new-stv 0.64 0.9))

(define RedBox1
    (EvaluationLink
         (GroundedPredicateNode "scm: redness")
         (ListLink (VariableNode "$X")
                    Red)
    )
)

(define RedBox2
   (EvaluationLink (stv 0.56 0.7)
         Red
         (ConceptNode "BB2")
   )
)

(define HerringBox1 (Evaluation (stv 0.3 0.8) Herring (ConceptNode "BB1")))
(define HerringBox2 (Evaluation (stv 0.3 0.8) Herring (ConceptNode "BB2")))

(define HerringAndRedBox1 (AndLink RedBox1 HerringBox1))
(define HerringAndRedBox2 (AndLink RedBox2 HerringBox2))
   

(define (run-bc and-box) 
    (define result (conj-bc and-box))
    (display "\n")
    (display result)
    (display (cog-tv (car (cog-outgoing-set result))))
    (display "\n")
)

(ure-logger-set-level! "debug")
(run-bc HerringAndRedBox1)
;(run-bc HerringAndRedBox2)
;(cog-evaluate! RedBox1)
