<template>
  <ul v-if="!tableLoading" class="header__filter header__filter--full-width">
    <li class="header__filter-item">
      <GridViewHide
        :database="database"
        :view="view"
        :fields="fieldsAllowedToBeHidden"
        :read-only="readOnly"
        :store-prefix="storePrefix"
      ></GridViewHide>
    </li>

    <!-- Add the ViewFilterForm component here -->
    <!-- <li class="header__filter-item">
      <ViewFilterForm
        ref="viewFilterForm"
        :fields="fields"
        :view="view"
        :read-only="readOnly"
        :disable-filter="disableFilter"
        @refresh="$emit('refresh', $event)"
      ></ViewFilterForm>
    </li> -->

    <li class="header__filter-item header__filter-item--right">
      <ViewSearch
        :view="view"
        :fields="fields"
        :store-prefix="storePrefix"
        @refresh="$emit('refresh', $event)"
      >
      </ViewSearch>
    </li>
  </ul>
</template>

<script>
import { mapState } from 'vuex'

import GridViewHide from '@baserow/modules/database/components/view/grid/GridViewHide'
import ViewSearch from '@baserow/modules/database/components/view/ViewSearch'

import ViewFilterForm from '@baserow/modules/database/components/view/ViewFilterForm'

export default {
  name: 'GridViewHeader',
  components: { GridViewHide, ViewSearch, ViewFilterForm },
  props: {
    database: {
      type: Object,
      required: true,
    },
    view: {
      type: Object,
      required: true,
    },
    fields: {
      type: Array,
      required: true,
    },
    readOnly: {
      type: Boolean,
      required: true,
    },
    storePrefix: {
      type: String,
      required: true,
    },
  },
  computed: {
    ...mapState({
      tableLoading: (state) => state.table.loading,
    }),
    fieldsAllowedToBeHidden() {
      return this.fields.filter((field) => !field.primary)
    },
  },

  //  mounted() {
  //    this.$nextTick(() => {
  //      // Call the addFilter method after the entire page has loaded
  //      this.$refs.viewFilterForm.addFilter()
  //    })
  //  },
}
</script>
