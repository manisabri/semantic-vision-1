
(load-from-path "conjunction-rule-base-config.scm")

(Concept "BB1")
(Concept "BoundingBox")

(Inheritance (Concept "BB1") (Concept "BoundingBox"))

(define Herring (Predicate "Herring"))
(define Red (Predicate "Red"))

(define RedBox1 (Evaluation (stv 0.4 0.9) Red (ConceptNode "BB1")))
(define HerringBox1 (Evaluation (stv 0.3 0.8) Herring (ConceptNode "BB1")))
(define HerringAndRedBox1 (And RedBox1 HerringBox1))

(define result (conj-bc HerringAndRedBox1))

(display (cog-tv (car (cog-outgoing-set result))))
