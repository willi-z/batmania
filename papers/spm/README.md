# Single Particle Model

This paper is one of the fundamental papers of single particle based battery modeling.
In this paper a particle of a single halfcell is simulated.
With only one differential equations it is one of the simplest models to start with.

Implementing the model of the paper seems straight forward, but comes with some pitfalls which have been addressed by this implementation.
The paper introduces the unitless concentration $y$, which at the beginning of the simulation (intial condition) is $=1$.
But the function of the open-circuit potential $U_{ocp}$ is singluar for $y$-values greater or equal to $y_{max} = 0.998432$.
This implementions goes arround the problem by using a linear function for $y >= y_{max}$  (Taylor expension).
Nevertheless $y$-values equal to 1 are still a problem, because the ion flux $j$ will be always zero.

## References
- [paper]()
- [vector calculus identities](https://en.wikipedia.org/wiki/Vector_calculus_identities)
