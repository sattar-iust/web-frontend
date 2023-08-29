<template functional>
  <div
    class="grid-view__cell"
    :class="{
      ...(data.staticClass && {
        [data.staticClass]: true,
      }),
      'cell-error': props.value === 'NaN',
    }"
  >
    <div class="grid-field-number">
      {{
        props.value && props.value !== 'NaN' && props.field.name.includes('€')
          ? (+props.value).toLocaleString(undefined, {
              style: 'currency',
              currency: 'EUR',
            })
          : props.value !== 'NaN'
          ? props.value
          : 'Invalid Number'
      }}
    </div>
  </div>
</template>
