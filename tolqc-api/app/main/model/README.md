# ToLQC Models

## Additional Model Mixins

N.B. the mixin(s) must come before **Base**/**EnumBase** in the inheritance arguments to the class definition.

### Extra fields

Models may support extra fields, that are not defined in the schema, by inheriting additionally from the **ExtFieldMixin**.

These can be added to, in POST/PATCH requests, by specifying key:value pairs that should be added in the
resource-level meta (see JSON:API spec), in a field named "ext".

### Log

Models can log changes to their data by additionally inheriting from the **LogMixin**.
