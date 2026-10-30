# Semgrep Security Assessment - Lab 01

## 1. Objective

Test Semgrep static application security testing (SAST)
against deliberately vulnerable Python code, apply a
remediation, and validate the result.

## 2. Tool and Configuration

- Tool: Semgrep CLI 1.183.0
- Primary ruleset: p/python
- Secrets ruleset: p/secrets
- Scan mode: Local CLI scan

## 3. Test Case A — OS Command Injection Risk

Affected file:
vulnerable-app/app.py

Affected code:
subprocess.run(user_input, shell=True)

Semgrep rule:
python.lang.security.audit.subprocess-shell-true.subprocess-shell-true

Risk:
Passing untrusted input to a shell can allow unintended
operating-system command execution.

Detection:
Semgrep detected one blocking finding using p/python.

## 4. Test Case B — Demonstration Password

Affected file:
vulnerable-app/app.py

Test code:
password = "demo-password-123"

Detection:
The selected p/secrets ruleset returned zero findings.

Interpretation:
This is an undetected test case, not a confirmed
Semgrep finding. A zero-finding result does not establish
that code contains no secrets. Detection depends on
rule coverage and the patterns used by the scanner.

## 5. Remediation

Remediated files:
- vulnerable-app/app_fixed.py
- secure-app/app.py

Changes:
- Replaced shell=True with shell=False.
- Passed command arguments as a list.
- Enabled check=True.

Security consideration:
Using an argument list with shell=False avoids shell
interpretation in this example. Production applications
should also restrict permitted commands, validate input,
and apply least-privilege execution. This example uses
echo for demonstration; it is not a general-purpose
command execution design.

## 6. Validation Results

### Vulnerable and remediated examples

Scan:
p/python against vulnerable-app/

Results:
- Files scanned: 2
- Rules applied: 151
- app.py: 1 blocking finding
- app_fixed.py: 0 findings

### Dedicated secure application

Scan:
p/python against secure-app/

Results:
- Files scanned: 1
- Rules applied: 151
- app.py: 0 findings

### Independent remediation scan

Scan:
p/python against vulnerable-app/app_fixed.py

Results:
- Files scanned: 1
- Rules applied: 151
- Findings: 0

## 7. Assessment Conclusion

Semgrep successfully detected the unsafe subprocess
shell invocation in the deliberately vulnerable example.

The corrected implementation produced no matching
findings under the selected 151 Python rules.

The demonstration password was not detected by the
selected secrets ruleset.

These results demonstrate a successful targeted
detection and remediation exercise. They do not
constitute a complete security audit or prove that
the application is free from vulnerabilities.

## 8. Next Steps

- Automate Semgrep scanning with GitHub Actions.
- Configure the workflow to fail when blocking findings
  are detected in secure-app/.
- Test the CI security gate with a controlled vulnerable
  code change.
- Preserve scan results and remediation evidence.
