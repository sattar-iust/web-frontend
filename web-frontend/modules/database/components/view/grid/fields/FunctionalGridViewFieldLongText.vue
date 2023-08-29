<template functional>
  <div class="grid-view__cell grid-field-long-text__cell">
    <div class="grid-field-long-text">
      <template
        v-if="
          props.value &&
          props.value.includes('@') &&
          props.field.name.includes('@')
        "
      >
        <a :href="'https://' + props.value.split('@')[1]" target="_blank">{{
          props.value.split('@')[0]
        }}</a>
      </template>
      <template v-else>
        {{ props.value }}
      </template>
    </div>
  </div>
</template>
