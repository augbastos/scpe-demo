# scpe-demo

A demo of [SCPE](https://github.com/augbastos/scpe), which verifies signed AI-use disclosures
for pull requests and shows which key signed them.

**[Pull request #3](https://github.com/augbastos/scpe-demo/pull/3)** is the one to read. A
signed contribution arrives as an ordinary pull request, carrying its attestation in the body;
the Action re-derives the diff from the branch, hashes it, fetches the signer's keys from
github.com, and posts the seal as a comment. The diff and its hash are recomputed from the
branch; the AI-use disclosure is a signed declaration by the contributor. Verifying its
signature identifies the signing key, but does not establish whether the declaration is true.

To be exact about what it demonstrates: the contribution was signed by SCPE's own author and
verified by SCPE's own verifier. It proves the path works end to end, in public. It does not
prove anyone else has used it, because nobody has.

`calc.py` is deliberately tiny — the kind of thing a first low-risk contribution fixes.

The workflow is the two-file template from the protocol repo:
[`scpe.yml`](.github/workflows/scpe.yml) verifies without secrets, and
[`scpe-seal.yml`](.github/workflows/scpe-seal.yml) posts the comment. `require` is `"false"`
here, configuring an informational seal rather than requiring a signed contribution.

The commit history predates the rename and still mentions an earlier project name. It is left
alone rather than rewritten, since rewriting the history of a repository that exists to
demonstrate tamper-evidence would be a strange thing to do.
