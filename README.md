<h3>Kestrel Solver Interface with AMPL</h3>
<p>
AMPL supports multiple usage modes for the Kestrel interface to the NEOS Server, allowing users to solve models remotely without installing solvers locally:
</p>
<ul>
  <li><a href="https://dev.ampl.com/solvers/kestrel/"><i><b>AMPL</b></i></a> &mdash; Solve models on NEOS by selecting <i>kestrel</i> as the solver directly in the AMPL environment.</li>
  <li><a href="https://dev.ampl.com/solvers/kestrel/"><i><b>Python (amplpy)</b></i></a> &mdash; Submit and solve AMPL models programmatically from Python, enabling integration with data pipelines, notebooks, and automated workflows.</li>
  <li><a href="https://dev.ampl.com/solvers/kestrel/"><i><b>Other APIs (R, C++, C#/.NET, Java, MATLAB)</b></i></a> &mdash; Access NEOS solvers through Kestrel for scripted or batch job submission from external applications.</li>
</ul>

<h4><i>Using Kestrel in Python</i></h4>

<pre style="background:#f6f8fa; padding:10px; border-radius:4px;">
<span style="color:#22863a"># Install Python API for AMPL:</span>
<span style="color:#6a737d">$</span> python -m pip install amplpy --upgrade

<span style="color:#22863a"># Install AMPL &amp; solver modules:</span>
<span style="color:#6a737d">$</span> python -m amplpy.modules install gokestrel  <span style="color:#22863a"># install Kestrel</span>

<span style="color:#22863a"># Activate your license (e.g., free https://ampl.com/start-free-now/):</span>
<span style="color:#6a737d">$</span> python -m amplpy.modules activate <span style="color:#a31515">&lt;<b>your-license-uuid</b>&gt;</span>
</pre>

<p>How to use:</p>
<pre style="background:#f6f8fa; padding:10px; border-radius:4px;">
<span style="color:#22863a"># Submit and solve a model on NEOS using Kestrel in Python</span>
<span style="color:#0000cc">from</span> amplpy <span style="color:#0000cc">import</span> AMPL
ampl = AMPL()

<span style="color:#22863a"># ... define model and data ...</span>

ampl.solve(
    solver=<span style="color:#a31515">"kestrel"</span>,
    kestrel_options=<span style="color:#a31515">"option1=value1 option2=value2"</span>)
</pre>

<h4><i>Using Kestrel in AMPL</i></h4>

<pre style="background:#f6f8fa; padding:10px; border-radius:4px;">
<span style="color:#6a737d">ampl:</span> <span style="color:#0000cc">option</span> solver kestrel;  <span style="color:#22863a"># change the solver</span>
<span style="color:#6a737d">ampl:</span> <span style="color:#0000cc">option</span> kestrel_options <span style="color:#a31515">'option1=value1 option2=value2'</span>;  <span style="color:#22863a"># specify options</span>
<span style="color:#6a737d">ampl:</span> <span style="color:#0000cc">solve</span>;  <span style="color:#22863a"># solve the problem</span>
</pre>
<p>
Complete documentation &mdash; including installation, configuration, supported solvers, and AMPL/Python/API examples &mdash; is available at: <a href="https://dev.ampl.com/solvers/kestrel/">https://dev.ampl.com/solvers/kestrel/</a>
