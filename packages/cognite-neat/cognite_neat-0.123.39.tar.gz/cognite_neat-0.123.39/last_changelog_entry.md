
### Improved

- Improved RAW extractor to convert all string values (not just nested)
to their ideal types and to generate only a single triple for
connection-type keys, eliminating redundant string-typed triples that
previously caused incorrect multi-type inferences.