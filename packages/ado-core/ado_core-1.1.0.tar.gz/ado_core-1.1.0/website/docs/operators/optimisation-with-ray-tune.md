<!-- markdownlint-disable code-block-style -->
<!-- markdownlint-disable-next-line first-line-h1 -->
## Overview

### What does the `ray_tune` operator do?

The `ray_tune` operator enables **running optimization algorithms on a
`discoveryspace`**. It uses the
[RayTune](https://docs.ray.io/en/latest/tune/index.html) framework, and most of
the capabilities of RayTune can be access via the operator without the need to
write python code.

`ray_tune` is an _explore_ operator.

### When should you use the `ray_tune` operator?

Use the `ray_tune` operator when you want to:

- **find the maximum or minimum value** of an observed property/target property
  in a `discoveryspace`
- efficiently sample a `discoveryspace` with respect to an observed
  property/target property i.e. sample to understand the distribution of that
  metric in the space

The `ray_tune` operator supports **memoization**: if it samples the same entity
twice, and that entity has already had the measurement space applied, it will
replay the already measured values (by default).

### Differences in using the `ray_tune` operator and RayTune directly

Using RayTune via the ado `ray_tune` operator brings the following advantages:

- Distributed storage and sharing of optimization runs and their results
- Automatic recording of provenance
- Transparent and distributed memoization
- Fully declarative interface, no need for programming

However, there are a few drawbacks:

- Some customizations that requires programming are not available
- The current `ado` generic actuator model is not compatible with some RayTune
  features which assume interaction with RayTrain.
  - See [early measurement stopping](#early-measurement-stopping) for more
    details.

### What happens if I apply multiple `ray_tune` operations to a space?

If you apply multiple `ray_tune` operations you just get multiple optimization
runs of the different lengths and types you have requested. This is the same
behaviour as applying RandomWalk multiple time to a space and is explained in
more detail in the
[RandomWalk documentation](random-walk.md#what-happens-if-i-apply-multiple-randomwalk-operations-to-a-space)

## Available Optimizers

The optimizers available depend on the RayTune version used. At time of writing
they are:

!!! info
    The ax optimizer has been removed due to incompatibilities
    with the latest numpy versions.

- hyperopt
- bayesopt
- bohb
- nevergrad
- optuna
- zoopt
- hebo

In addition `ado` adds a
[additional optimizer called `lhu_sampler`](#ado-additions-to-raytune).

!!! important end

    The above names are used to specify the optimizer to use in an operation.

    The names are defined by RayTune: check
    [the raytune docs](https://docs.ray.io/en/latest/tune/api/doc/ray.tune.search.create_searcher.html#ray.tune.search.create_searcher)
    for the current list of optimizer names. The list is also defined by in the
    variable `ray.tune.search.SEARCH_ALG_IMPORT`

!!! warning end

    RayTune also defines python classes for each optimizer. These class names are
    NOT the same as the "optimizer names" it defines and cannot be used with `ado`

### Installing an optimizer

Each optimizer is its own python package and RayTune does not install them by
default. `ado` installs `bayesian-optimization` and `nevergrad` but if you want
to use any of the others you must install their corresponding python package.
For example to use `bohb` run:

```commandline
pip install hpbandster ConfigSpace
```

## Setting the parameters of a `ray_tune` operation

When configuring a `ray_tune` operation there are three groups of parameters to
consider:

- [Tuning Configuration](#tune-config): general optimization parameters
  - This includes specific
    [Optimizer Parameters](#optimizer-parameters-search_algparams)
- [Runtime Configuration](#run-config): parameters related to RayTune, for
  example where its stores data
  - This includes the [Stopper Configuration](#stoppers) that determines if an
    optimization should stop
- [Orchestrator Configuration](#orchestrator-config): parameters related to
  `ado`

For example, the default parameters and values for a `ray_tune` operation are:

<!-- markdownlint-disable line-length -->
```yaml
orchestratorConfig:
  failed_metric_value: None # This will be used for the value of "metric' for any entities where it could not be measured (for any reason)
  result_dump: none # If specified the best result found will be written to this file
  single_measurement_per_property: true # If true memoization is used. If false already measured entities will be re-measured.
runtimeConfig:
  stop: None # A list of Stoppers or None. See below for stoppers
tuneConfig:
  metric: wallclock_time # The target property identifier to optimize w.r.t
  mode: min # Whether to search for min or max of the target property
  num_samples: 1 # The number of samples to draw
  search_alg:
    name: ax # The name of the optimization algorithm to use
    params: {} # The parameters for the optimizer
```
<!-- markdownlint-enable line-length -->

The following sections describes each of these parameter sets in more detail. As
you go through these sections it is worth referring to the
[comprehensive example](#example) that demonstrate putting all the pieces
together and how they interact.

!!! info end

    You can get a default RayTune operation template and the schema of its
    parameters by running
    `ado template operation --operator-name ray_tune --include-schema` The
    information output by this command should always be preferred over the
    information presented here if there is an inconsistency.

### Trials versus Samples

In RayTune `samples` means the points to measure, and `trials` are measurements
of those points. They are related to `ado` concepts of `entities` (samples) and
`measurements` (trials).

### Orchestrator Config

The `orchestratorConfig` section currently supports the following parameters,
which are all optional:

- `failed_metric_value` (default None)
  - This will be used for the value of "metric' for any entities where it could
    not be measured (for any reason)
- `result_dump (default None)
  - If specified the best result found will be written to this file
- `single_measurement_per_property` (default true)
  - If true
    [memoization](#what-happens-if-i-apply-multiple-ray_tune-operations-to-a-space)
    is used. If false already measured entities will be re-measured.

### Tune Config

The `tuneConfig` section supports many of the
[parameters of the `ray.tune.TuneConfig` class](https://docs.ray.io/en/latest/tune/api/doc/ray.tune.TuneConfig.html).

**Supported parameters:**

- `metric` (required)
  - The
    [target property identifier](../core-concepts/actuators.md#target-and-observed-properties)
    to optimize.
- `mode` (required)
  - `min` or `max`: Whether to search for min or max of the target property
- `search_alg` (required)
  - **Note**: This must be an [optimizer name](#available-optimizers) c.f. in
    RayTune it would be an optimizer instance
- `num_samples` (defaults to 1)
  - **Note**: The exact interpretation of `num_samples` is optimizer dependent
    e.g. some do not count "warm-up" samples as part of this.
- `max_concurrent_trials`
  - **Note**: this can also be controlled via most optimizers parameters. If not
    set, the default value depends on the optimizer
- `time_budget_s`: How many second to run the optimizer for

**Unsupported parameters:**

- `scheduler` - _Coming soon_
- `reuse_actors` - not relevant
- `trial_name_creator` - not relevant
- `trail_dirname_creator` - not relevant

### Optimizer Parameters (search_alg.params)

The optimizer parameters are given as a dictionary to the
`tuneConfig.search_alg.params` field.

The parameters available for a given optimizer are detailed in the
[ray tune documentation for that optimizer.](https://docs.ray.io/en/latest/tune/api/suggestion.html)
Almost all parameters that are listed in the RayTune docs for creating an
instance of an optimizer can be specified in `tuneConfig.search_alg.params`.
However, there are a few that should not be set. This is discussed in
[parameters to omit](#parameters-to-omit).

!!! info end

    The dictionary value you set for `tuneConfig.search_alg.params`
    will be used to initialise the optimizer in the standard python manner:

    ```python
    optimizerInstance = optimizerClass(**params)
    ```

!!! info end

    Currently you cannot obtain a given optimizers parameters are via `ado`. To
    understand the configuration possibilities for an optimizer you must check the
    RayTune documentation.

#### Parameters to omit

All RayTune optimizers have the parameters `space`, `metric` and `mode` which
should be **omitted** from the `tuneConfig.search_alg.params` dictionary.

The `space` parameter will be filled by `ado` based on the `discoveryspace` the
`ray_tune` operation is being applied to.

The `metric` and `mode` parameters are provided via the `tuneConfig` fields (see
above).

#### Common parameters

All RayTune optimizers support a parameter `points_to_evaluate` which is a list
of the initial entities to test. Each entity is described by a dictionary of
"[constitutive property id](../core-concepts/entity-spaces.md#entities)/"value"
pairs.

!!! warning end

    The constitutive property identifiers and values must be compatible with the
    `discoveryspace` the operation is being applied to. If they are not an XXXXX
    exception will be raised when the operation starts.

For example:

```yaml
- model_name: granite-3b
  number_gpus: 4
  tokens_per_sample: 2048
  gpu_model: A100-SXM4-80GB
```

#### Optimizer specific parameters

In addition to `points_to_evaluate` each optimizer has its own parameters. For
example, some optimizers allow evaluating multiple points at same time, while
others have a warm-up period of random sampling that can set. Check the
[RayTune documentation for each optimizer](https://docs.ray.io/en/latest/tune/api/suggestion.html)
to understand the available options.

!!! info warning

    `ado` does not perform any validation of the optimizer parameters.
    Validation will be performed by RayTune when creating the optimizer class

#### nevergrad parameters

The nevergrad search algorithm has a required parameter `optimizer` that
programmatically is set to a nevergrad optimizer class or instance. In `ado` set
this value to the string name of the optimizer. This valid strings are the keys
of the nevergrad registry, which you can see with:

```python
import nevergrad
print(list(nevergrad.optimizers.registry.keys()))
```

### Run Config

The `runConfig` section supports many of the
[parameters of the `ray.tune.RunConfig` class](https://docs.ray.io/en/latest/train/api/doc/ray.train.RunConfig.html).
All are optional although the above template shows `stop` as this is the most
relevant

Many of the run config parameters are related to storing the RayTune runs on
disk. Since `ado` automatically stores the results and operation details in
`samplestore` and `metastore` you likely do not need to set any of these values.

**Key Supported Parameters:**

- `stop` - see [Stoppers](#stoppers)
- `storage_path`:
  - `ado` defaults this to "/tmp/ray_results" as this directory is writable in
    the default `ado` image used in ray clusters.
    - If you change this path ensure it is writable

**Other supported parameters:**

- `name`
- `storage_filesystem`
- `verbose`

**Unsupported parameters:**

These parameters are mostly for use with RayTrain (using tune as train
hyperparameter search). As such they are specific to the use case of model
training.

- `failure_config`
- `checkpoint_config` - for RayTrain, not relevant here
- `sync_config`

### Stoppers

Stoppers define conditions for stopping an optimization. An example includes
stopping when no new min/max have been found after N samples.

An optimization run can specify any number of stoppers and the optimization will
stop whenever the condition of any stopper in the list is met.

You specify the stoppers to use as a list to the `runConfig.stop` field. Each
stopper in the list is defined using the following yaml.

```yaml
name: #The name of the stopper class
positionalParams: #The positional params of the stopper: a list of strings/numbers
keywordParams: #The keyword params of the stopper: a dictionary of key/value pairs
```

!!! info end

    Its recommend to use `keywordParams` even for positional parameters

The following sections describe the available stoppers.

#### RayTune stoppers

RayTune
[provides a number of Stoppers](https://docs.ray.io/en/latest/tune/api/stoppers.html).
Some of these, MaximumIterationStopper, ExperimentPlateauStopper and
TrialPlateauStopper, are for early measurement stopping when using RayTrain and
have no effect when used via `ado`.

Of the remaining stoppers TimeoutStopper is automatically used if you specify
[`tuneConfig.time_budget_s`](#tune-config) so it does not have to specified
independently. Similarly, CombinedStopper is automatically used if you specify
more than one `stopper` in the list given to `runConfig.stop`.

Finally, FunctionStopper, which allows passing a custom python function as a
stopper, cannot currently be used with `ado`.

#### `ado` stoppers

`ado` provides four inbuilt stoppers:

- SimpleStopper: Stops if no improvement in the target metric after N steps
- GrowthStopper: Stops when the improvement in the target metric is less than a
  threshold for N steps
- MaxSamplesStopper: Stops when a certain number of samples have been drawn. Is
  less ambiguous than `tuneConfig.num_samples`
- InformationGainStopper: Stops when samples are no longer providing significant
  additional information on how the constitutive properties of the entity space
  are related to the target property.

<!-- markdownlint-disable descriptive-link-text -->
Each of these are described in more detail, along with their parameters,
[here](#ado-additions-to-raytune).
<!-- markdownlint-enable descriptive-link-text -->

#### Example

This example shows using `SimpleStopper` to stop an optimization when the metric
has not improved after 10 trials. It will allow 5 trials to be performed before
checking if it should stop the optimization, and will consider trials returning
`nan` for the metric towards the 10 trial budget. It combines this with
`MaxSamplesStopper` to stop when 50 samples have been drawn.

```yaml
stop:
  - name: SimpleStopper
    keywordParams:
      metric: wallclock_time
      min_trials: 5
      buffer_states: 10
      count_nan: True
  - name: MaxSamplesStopper
    keywordParams:
      max_samples: 50
```

#### Early Measurement Stopping

Some RayTune stoppers directly support the case where each trial (measurement)
is a RayTrain job. These [stoppers](#stoppers) can inspect the progress of an
individual RayTrain jobs i.e. intermediate metric values, to determine if a
trial should be stopped. This ability assumes particular behaviour of such a job
e.g. the trial is generating a timeseries of the metric being optimized.

Currently, `ado`s actuator model does not assume there are intermediate values
of a metric being measured by an experiment, or provide a way to expose them.
Instead, we leave these domain specific details to the actuator. For example, in
`ado`s current model the actuator can implement and/or expose early-stopping if
it is possible.

### Example operation YAML

Here is an example ray_tune `operation` YAML for finding the workload
configuration with the fastest throughput for fine-tuning performance using the
SFTTrainer actuator:

- using the Nevergrad optimizer
- the [GrowthStopper](#growthstopper) to stop if no improvement found after 10
  steps, where improvement means a configuration that is faster by more than 20
  tokens per second
- the [MaxSamplesStopper](#maxsamplestopper) to stop once 50 configurations have
  been searched
- a time budget of 2 hours
- specifying [initial point to sample](#common-parameters)

<!-- markdownlint-disable line-length -->
```yaml
runtimeConfig:
  stop:
    - name: GrowthStopper
      keywordParams:
        mode: max
        metric: dataset_tokens_per_second
        growth_threshold: 20 #if the change is less than 20 tokens per second consider the optimization not improving
        grace_trials: 10
    - name: MaxSamplesStopper
      keywordParams:
        max_samples: 50
tuneConfig:
  metric: dataset_tokens_per_second
  mode: min
  num_samples: 50 # The number of samples to draw.
  time_budget_s: 7200
  search_alg:
    name: nevergrad # The name of the optimization algorithm to use
    params:
      optimizer: "CMA"
      points_to_evaluate:
        - model_name: granite-3b
          number_gpus: 4
          model_max_length: 2048
          gpu_model: A100-SXM4-80GB
```
<!-- markdownlint-enable line-length -->

## `ray_tune` operation output

### Seeing the optimal configuration found

A successful `ray_tune` operation will create a `datacontainer` resource,
containing information from RayTune on the best configuration found.

To get the id of the `datacontainer` related to a ray_tune `operation` resource
with id $OPERATION_IDENTIFIER use:

```commandline
ado show related operation $OPERATION_IDENTIFIER
```

This will output something like:

```commandline
datacontainer
  - datacontainer-d6a6501b
discoveryspace
  - space-047b6a-f60613
```

To see the best point found (and in general the contents of the datacontainer)
use the `describe` CLI command:

```commandline
ado describe datacontainer $DATACONTAINER_ID
```

For a `datacontainer` created by a `ray_tune` operation, an example output is:

```commandline
Identifier: datacontainer-d6a6501b
Basic Data:

  Label: best_result

  {'config': {'x2': -1.1192905253425014,
    'x1': 2.081208150586974,
    'x0': 0.5621591414422049},
   'metrics': {'function_value': 20.788056393697595,
    'timestamp': 1756804287,
    'checkpoint_dir_name': None,
    'done': True,
    'training_iteration': 1,
    'trial_id': '7a7153ed',
    'date': '2025-09-02_10-11-27',
    'time_this_iter_s': 1.0576610565185547,
    'time_total_s': 1.0576610565185547,
    'pid': 52036,
    'hostname': 'Michaels-MacBook-Pro-2.local',
    'node_ip': '127.0.0.1',
    'config': {'x2': -1.1192905253425014,
     'x1': 2.081208150586974,
     'x0': 0.5621591414422049},
    'time_since_restore': 1.0576610565185547,
    'iterations_since_restore': 1,
    'experiment_tag': '40_x0=0.5622,x1=2.0812,x2=-1.1193'},
   'error': None}
```

We can see here that the point found is
`{'x2': -1.1192905253425014, 'x1': 2.081208150586974, 'x0': 0.5621591414422049}`
where `function_value` was ~20.8.

### Optimization path

To see all the configurations (entities) visited during an optimization
operation $OPERATION_IDENTIFIER run

```commandline
ado show entities operation $OPERATION_IDENTIFIER
```

> [!NOTE]
>
> This command also works during an operation. It shows up to the most recent
> measured entity.

## ado additions to RayTune

`ado` adds one optimizer and a selection of stoppers to those offered by RayTune

### Latin Hypercube Sampler

The `lhu_sampler` samples a `discoveryspace` using
[latin hypercube sampling](https://en.wikipedia.org/wiki/Latin_hypercube_sampling).
This is a method for "almost" randomly sampling a space while ensuring the
samples are evenly spaced across the space. Using the `lhu_sampler` you can
potentially get more information about the variance of a metric across a space
with fewer samples than fully random sampling. It also reduces chances of not
exploring dimensions in high-dimensional spaces when sampling budget is limited.

The `lhu_sampler` pairs well with the
[InformationGainStopper](#informationgainstopper)

Configuration the `lhu_sampler` follows the same pattern as those for other
[optimizer parameters](#optimizer-parameters-search_algparams). For the
`lhu_sampler`, there is only one optional parameter,
[points_to_evaluate](#common-parameters).

```yaml
name: "lhu_sampler"
params:
  points_to_evaluate:
    - model_name: granite-3b
      number_gpus: 4
      tokens_per_sample: 2048
      gpu_model: A100-SXM4-80GB
    - model_name: granite-3b
      number_gpus: 2
      tokens_per_sample: 2048
      gpu_model: A100-SXM4-80GB
```

### MaxSampleStopper

Stops an optimization after N samples/trials.

The following YAML describes the stoppers parameters. Parameters without values
are required.

<!-- markdownlint-disable line-length -->
```yaml
name: MaxSamplesStopper
keywordParams:
  max_samples: 10 # Will stop the optimization when this number of samples have been measured. Required
```
<!-- markdownlint-enable line-length -->

### SimpleStopper

Stops an optimization when the metric has not improved after N steps. Note, its
excepted `mode` and `metric` should match the corresponding
[`tuneConfig`](#tune-config) parameters but this is not checked.

The following YAML describes the stoppers parameters. Parameters without values
are required.

<!-- markdownlint-disable line-length -->
```yaml
name: SimpleStopper
keywordParams:
  mode: # `min` or `max`: Whether to search for min or max of the target property/metric. Required
  metric: # The target property being optimized. Required.
  min_trials: 5 # The number of trials to perform (samples to take) before applying any stopping criteria
  buffer_states: 2 # The number of samples/optimization steps to wait before declaring no improvement.
  stop_on_repeat: True # If True, the stopper will stop the optimization if it sees the same sample twice.
  count_nan: True # If True, samples measuring 'nan' count towards the steps to wait before declaring no improvement.
```
<!-- markdownlint-enable line-length -->

!!! important end

    `buffer_states` does not reset if the metric is observed to improve in a step.
    That is, it is the _total_ number of samples allowed that do not improve on the
    best found sample.

### GrowthStopper

Stops an optimization once it sees the metric improvement rate is below a
threshold. This differs to SimpleStopper which as long as there is any
improvement won't stop the optimization.

- if the metric value gets worse on a step, i.e. negative improvement, it is
  considered to be below the threshold.
- Samples whose metric value is `nan` are always included

The following YAML describes the stoppers parameters. Parameters without values
are required.

<!-- markdownlint-disable line-length -->
```yaml
name: GrowthStopper
keywordParams:
  mode: # `min` or `max`: Whether to search for min or max of the target property/metric. Required
  metric: # The target property being optimized. Required.
  growth_threshold: 1.0 # If the difference in two samples is less than this threshold the optimization is considered to be not improving
  grace_trials: 2 # The number of samples/optimization steps to wait before declaring the metric is not improving. Same as buffer_states for SimpleStopper.
```
<!-- markdownlint-enable line-length -->

!!! important end

    `grace_trials` does not reset if the metric is observed to "grow" in a step
    after it was observed to not "grow" That is, it is the _total_ number of samples
    allowed where the improvement in the metric is less than threshold.

### InformationGainStopper

This stopper criteria is based on Mutual Information, which here is used to
measures how related the constitutive properties (dimensions of the entity
space) are to the metric being optimized. At a high-level this stopper stops
when it observes the mutual information is converging.

This stopper considers two ways that the mutual information can change:

1. **mutual information value**: If the value is changing by less than a
   threshold it is considered "converging"
2. **properties contribution to the mutual information**: This can be measured
   in two ways:
   1. Change in the ranking of which constitutive properties contribute the most
      to the mutual information with the metric. If the ranking is not changing
      the mutual information is considered to be converging.
   2. Change in the set of constitutive properties which contribute most to the
      mutual information with metric. If the set of propertiers is not changing
      the mutual information is considered to be converging.

The stopper will only stop when it sees _both_ the **mutual information value**
and the **properties that contribute to it** converging.

This stopper will perform at least
`2x(number of constitutive properties in entity space)` samples before applying
its stopping criteria.

The following YAML describes the stoppers parameters. Parameters without values
are required.

<!-- markdownlint-disable line-length -->
```yaml
name: InformationGainStopper
keywordParams:
  mi_diff_limit: # If the mutual information increase on addition of the latest sample is less than this value, it counts as "converging".
  samples_below_limit: # # The number of samples/optimization steps to wait before declaring the mutual information is not increasing. Similar to buffer_states for SimpleStopper.
  consider_pareto_front_convergence: # If True the stopper considers convergence of the set of important properties (2.2 above). If False it considers the ranking (2.1 above)
```
<!-- markdownlint-enable line-length -->

!!! important end

    Both the mutual information value **and** the property ranking/set must stay
    unchanged for `samples_below_limit` for the stopping criteria to be reached

## What's next

<!-- markdownlint-disable line-length -->
<!-- markdownlint-disable-next-line no-inline-html -->
<div class="grid cards" markdown>

- :octicons-workflow-24:{ .lg .middle } **Try Searching for the Best Configurations**

      ---

      Try our example of using `ray_tune` [to search for best configurations](../examples/best-configuration-search.md).

      [Best configuration search example :octicons-arrow-right-24:](../examples/best-configuration-search.md)

- :octicons-rocket-24:{ .lg .middle } **Try Latin Hyper-Cube Sampling**

    ---

    Learn how to use [Latin Hyber-Cube Sampling and the InformationGainStopper](../examples/lhu.md) to discover important workload parameters.

    [Latin Hyper-Cube sampler example :octicons-arrow-right-24:](../examples/lhu.md)

</div>
<!-- markdownlint-enable line-length -->